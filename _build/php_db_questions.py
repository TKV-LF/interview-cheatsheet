"""PHP and MySQL cards: indexes, joins, race conditions, and engineering prompts."""

EXTRA = [
    {
        "id": "new-php-index",
        "page": "php",
        "section": "MySQL",
        "title": "When do you add an index?",
        "hint": "Say the query, then the columns. Not every column.",
        "q_en": "When do you add an index, and when do you refuse?",
        "a_en": """<p>I add an index for a query that is slow and that people actually run. The columns match the WHERE and the JOIN, in that order, then the ORDER BY if it still fits. Writes pay for every index, so I do not index a column because it “might be useful later”.</p>
<p>Example: the sales list of partner cases, always filtered by partner and status, newest first:</p>
<pre>SELECT id, status, created_at
FROM cases
WHERE partner_id = 42 AND status = 'open'
ORDER BY created_at DESC
LIMIT 50;</pre>
<p>That wants <code>(partner_id, status, created_at)</code>. A separate index on <code>status</code> alone does not help this query much. At Base the tax and payroll tables were large enough that a missing index was a real delay, not a textbook note.</p>""",
        "q_vi": "Khi nào bạn thêm index, và khi nào thì không?",
        "a_vi": """<p>Tôi thêm index cho query chậm mà người ta thật sự chạy. Cột khớp WHERE và JOIN, theo thứ tự đó, rồi ORDER BY nếu còn vừa. Mỗi index làm chậm ghi, nên tôi không index một cột vì “sau này có thể cần”.</p>
<p>Ví dụ: danh sách case của sales, lúc nào cũng lọc theo đối tác và trạng thái, mới nhất trước:</p>
<pre>SELECT id, status, created_at
FROM cases
WHERE partner_id = 42 AND status = 'open'
ORDER BY created_at DESC
LIMIT 50;</pre>
<p>Cần <code>(partner_id, status, created_at)</code>. Một index chỉ trên <code>status</code> hầu như không giúp query này. Ở Base, bảng thuế và lương đủ lớn để thiếu index là chậm thật, không phải ghi chú trong sách.</p>""",
        "notes": "<p><strong>Know:</strong> Index the query you have, not every column.</p><p><strong>Trap:</strong> Adding five indexes before EXPLAIN.</p>",
    },
    {
        "id": "new-php-composite",
        "page": "php",
        "section": "MySQL",
        "title": "Composite index, leftmost prefix",
        "hint": "Walk a warehouse lookup. They will ask why the second column is unused.",
        "q_en": "You have INDEX (warehouse_id, sku). Which queries use it?",
        "a_en": """<p>A composite index is read from the left. <code>(warehouse_id, sku)</code> is useful when <code>warehouse_id</code> is in the WHERE. It is not useful when you only filter by SKU.</p>
<pre>-- uses the index
WHERE warehouse_id = 3 AND sku = 'TS-451'
WHERE warehouse_id = 3

-- does not use this index
WHERE sku = 'TS-451'

-- also does not use a normal B-tree
WHERE sku LIKE '%451%'</pre>
<p>If partners search by SKU across every warehouse, they need an index that starts with <code>sku</code>, or a separate one. I would look at EXPLAIN before I add the second index. A leading <code>%</code> in LIKE will not use a B-tree either. That search belongs in a search engine, or at least a full-text index, not a hope.</p>""",
        "q_vi": "Có INDEX (warehouse_id, sku). Query nào dùng được?",
        "a_vi": """<p>Index kép đọc từ trái sang. <code>(warehouse_id, sku)</code> hữu ích khi WHERE có <code>warehouse_id</code>. Chỉ lọc SKU thì không dùng được.</p>
<pre>-- dùng index
WHERE warehouse_id = 3 AND sku = 'TS-451'
WHERE warehouse_id = 3

-- không dùng index này
WHERE sku = 'TS-451'

-- B-tree thường cũng không dùng
WHERE sku LIKE '%451%'</pre>
<p>Nếu đối tác tìm SKU trên mọi kho, cần index bắt đầu bằng <code>sku</code>, hoặc một index riêng. Tôi xem EXPLAIN trước khi thêm index thứ hai. <code>LIKE</code> với <code>%</code> đứng đầu không dùng B-tree. Kiểu tìm đó thuộc search engine, hoặc full-text, không phải hy vọng.</p>""",
        "notes": "<p><strong>Know:</strong> Leftmost prefix. LIKE '%x' is not an index lookup.</p><p><strong>Trap:</strong> Claiming one composite index covers every filter.</p>",
    },
    {
        "id": "new-php-join",
        "page": "php",
        "section": "MySQL",
        "title": "INNER JOIN versus LEFT JOIN",
        "hint": "Use a case list. Say which rows disappear.",
        "q_en": "When do you INNER JOIN, and when do you LEFT JOIN?",
        "a_en": """<p>INNER JOIN keeps rows that match on both sides. LEFT JOIN keeps every row on the left, and fills the right with NULL when there is no match.</p>
<p>A sales list of open cases with the partner name is an inner join. A case without a partner should not show up:</p>
<pre>SELECT cases.id, partners.name, cases.status
FROM cases
INNER JOIN partners ON partners.id = cases.partner_id
WHERE cases.status = 'open'
ORDER BY cases.created_at DESC
LIMIT 50;</pre>
<p>A report of every partner, including partners who have never opened a case, is a left join from partners to cases. If I INNER JOIN there, silent partners vanish and the report lies. I put the filter in SQL. I do not load every case into PHP and join in a loop. That is how N+1 starts.</p>""",
        "q_vi": "Khi nào INNER JOIN, khi nào LEFT JOIN?",
        "a_vi": """<p>INNER JOIN giữ dòng khớp cả hai bên. LEFT JOIN giữ mọi dòng bên trái, bên phải thành NULL khi không khớp.</p>
<p>Danh sách case đang mở kèm tên đối tác là inner join. Case không có đối tác thì không hiện:</p>
<pre>SELECT cases.id, partners.name, cases.status
FROM cases
INNER JOIN partners ON partners.id = cases.partner_id
WHERE cases.status = 'open'
ORDER BY cases.created_at DESC
LIMIT 50;</pre>
<p>Báo cáo mọi đối tác, kể cả người chưa mở case, là left join từ partners sang cases. Nếu INNER JOIN ở đó, đối tác im lặng biến mất và báo cáo nói dối. Filter để trong SQL. Tôi không kéo hết case vào PHP rồi join trong vòng lặp. Đó là chỗ N+1 bắt đầu.</p>""",
        "notes": "<p><strong>Know:</strong> INNER drops unmatched rows. LEFT keeps the left side.</p><p><strong>Trap:</strong> Joining in PHP after SELECT *.</p>",
    },
    {
        "id": "new-php-explain",
        "page": "php",
        "section": "MySQL",
        "title": "How you read EXPLAIN",
        "hint": "type ALL versus ref. Then Extra.",
        "q_en": "A query is slow. What do you look for in EXPLAIN?",
        "a_en": """<p>I run <code>EXPLAIN</code> on the real query, with realistic values, not <code>WHERE id = 1</code>. I look at three things. <code>type</code>: <code>ALL</code> is a table scan. At hundreds of thousands of rows that is the bug. <code>ref</code> or <code>range</code> means it is using an index. <code>rows</code>: how many rows MySQL thinks it will read. If it says 400,000 for a page of 50, the index is wrong. <code>Extra</code>: <code>Using filesort</code> or <code>Using temporary</code> often means ORDER BY or GROUP BY has no matching index.</p>
<p>Then I change one thing — the index or the query — and I EXPLAIN again. I do not add a cache on top of a scan. On Base PIT this is how a report stopped reading the whole tax table for one company.</p>""",
        "q_vi": "Query chậm. Bạn nhìn gì trong EXPLAIN?",
        "a_vi": """<p>Tôi chạy <code>EXPLAIN</code> trên query thật, với giá trị giống production, không phải <code>WHERE id = 1</code>. Tôi nhìn ba thứ. <code>type</code>: <code>ALL</code> là quét bảng. Hàng trăm nghìn dòng thì đó là bug. <code>ref</code> hoặc <code>range</code> nghĩa là đang dùng index. <code>rows</code>: MySQL nghĩ sẽ đọc bao nhiêu dòng. Nếu nó nói 400.000 cho một trang 50, index sai. <code>Extra</code>: <code>Using filesort</code> hoặc <code>Using temporary</code> thường là ORDER BY hoặc GROUP BY không có index khớp.</p>
<p>Rồi tôi đổi một thứ — index hoặc query — và EXPLAIN lại. Tôi không phủ cache lên một lần quét. Ở Base PIT, cách này khiến report thôi đọc cả bảng thuế cho một công ty.</p>""",
        "notes": "<p><strong>Know:</strong> type, rows, Extra. Change one thing, EXPLAIN again.</p><p><strong>Trap:</strong> EXPLAIN on a tiny local dump, then claiming production is fine.</p>",
    },
    {
        "id": "new-php-race",
        "page": "php",
        "section": "MySQL",
        "title": "Race condition on the last unit",
        "hint": "Two requests. One stock row. Speak the SQL.",
        "q_en": "Two sales users reserve the last unit at the same time. What happens?",
        "a_en": """<p>If each request reads quantity 1, then both write 0, you sold the same unit twice. The check and the write have to be one transaction, with a lock on that row:</p>
<pre>START TRANSACTION;
SELECT qty FROM stock WHERE sku = 'TS-451' FOR UPDATE;
-- if qty &gt;= 1
UPDATE stock SET qty = qty - 1 WHERE sku = 'TS-451';
INSERT INTO reservations (sku, case_id) VALUES ('TS-451', 88);
COMMIT;</pre>
<p>Without <code>FOR UPDATE</code>, both SELECTs see 1. I keep the transaction short. I do not call an email API while the lock is held. The same shape fits partner approval: lock the application, refuse a second approve. I would test with two parallel requests, not one happy click. I have not run a warehouse at QNAP’s scale. I have seen the same class of bug on workflow status and on payroll rows that must not be written twice.</p>""",
        "q_vi": "Hai sales giữ chiếc cuối cùng cùng lúc. Chuyện gì xảy ra?",
        "a_vi": """<p>Nếu mỗi request đọc quantity 1, rồi cả hai ghi 0, bạn bán cùng một chiếc hai lần. Bước kiểm tra và bước ghi phải nằm trong một transaction, và lock đúng dòng đó:</p>
<pre>START TRANSACTION;
SELECT qty FROM stock WHERE sku = 'TS-451' FOR UPDATE;
-- nếu qty &gt;= 1
UPDATE stock SET qty = qty - 1 WHERE sku = 'TS-451';
INSERT INTO reservations (sku, case_id) VALUES ('TS-451', 88);
COMMIT;</pre>
<p>Không có <code>FOR UPDATE</code>, cả hai SELECT đều thấy 1. Transaction để ngắn. Tôi không gọi API gửi mail khi đang giữ lock. Cùng hình dạng cho duyệt hồ sơ: lock đơn, từ chối lần duyệt thứ hai. Tôi sẽ test bằng hai request song song, không phải một cú click đúng đường. Tôi chưa chạy kho ở quy mô QNAP. Tôi đã gặp cùng loại bug trên trạng thái workflow và trên dòng lương không được ghi hai lần.</p>""",
        "notes": "<p><strong>Know:</strong> FOR UPDATE inside a short transaction.</p><p><strong>Trap:</strong> Check in PHP, then UPDATE with no lock.</p>",
    },
    {
        "id": "new-php-offset",
        "page": "php",
        "section": "MySQL",
        "title": "OFFSET pagination versus keyset",
        "hint": "Page 1 is fine. Page 2000 is not.",
        "q_en": "Why is LIMIT 50 OFFSET 100000 slow?",
        "a_en": """<p>MySQL still walks those 100,000 rows, then throws them away, then returns 50. Page one of a sales list is fine with OFFSET. A deep page, or an export that “pages” through the whole table, is not.</p>
<pre>-- cheap for page 1
LIMIT 50 OFFSET 0

-- expensive at scale
LIMIT 50 OFFSET 100000

-- keyset: remember the last id you showed
WHERE id &gt; 18420
ORDER BY id
LIMIT 50;</pre>
<p>For a UI I keep OFFSET for the first few pages and I disable “jump to page 500”. For a job that must visit every row, I walk by id ranges, the same way I chunked payroll and tax work at Base. I do not load 500,000 rows into PHP to paginate there.</p>""",
        "q_vi": "Vì sao LIMIT 50 OFFSET 100000 chậm?",
        "a_vi": """<p>MySQL vẫn đi qua 100.000 dòng đó, rồi bỏ, rồi trả 50. Trang một của danh sách sales thì OFFSET ổn. Trang sâu, hoặc export “lật trang” cả bảng, thì không.</p>
<pre>-- rẻ ở trang 1
LIMIT 50 OFFSET 0

-- đắt khi lớn
LIMIT 50 OFFSET 100000

-- keyset: nhớ id cuối cùng đã hiện
WHERE id &gt; 18420
ORDER BY id
LIMIT 50;</pre>
<p>Với UI tôi giữ OFFSET vài trang đầu và không cho “nhảy tới trang 500”. Với job phải đi hết từng dòng, tôi đi theo khoảng id, cùng cách tôi cắt nhỏ việc lương và thuế ở Base. Tôi không kéo 500.000 dòng vào PHP để phân trang ở đó.</p>""",
        "notes": "<p><strong>Know:</strong> OFFSET scans and discards. Keyset walks from the last key.</p><p><strong>Trap:</strong> Paginate in PHP after SELECT *.</p>",
    },
    {
        "id": "new-php-magic",
        "page": "php",
        "section": "Common questions",
        "title": "Magic link login",
        "hint": "Engineering prompt. Security first, Laravel second.",
        "q_en": "How would you implement a magic-link login?",
        "a_en": """<p>The user types an email. I do not put a password on that flow. I create a random token, I store only a hash of it, I set a short expiry — minutes, not days — and I email a link that carries the raw token once. When they click, I hash what arrived, find a row that is unused and not expired, start a session, and I invalidate the token so it cannot be replayed. HTTPS only. Rate-limit the “send link” endpoint so nobody mails a stranger a thousand times. The response is the same whether the email exists or not, so I do not leak accounts. I log the send and the consume, with an ip, so a stolen mailbox is visible. Laravel Mail plus a signed URL can carry this. The important part is one-time, hashed, short-lived, not the helper name.</p>""",
        "q_vi": "Bạn làm đăng nhập magic link thế nào?",
        "a_vi": """<p>User nhập email. Flow này không có password. Tôi tạo token ngẫu nhiên, chỉ lưu bản hash, hạn ngắn — vài phút, không phải vài ngày — và gửi mail một link mang token thô một lần. Khi họ bấm, tôi hash cái nhận được, tìm dòng chưa dùng và chưa hết hạn, mở session, rồi hủy token để không dùng lại. Chỉ HTTPS. Rate-limit endpoint “gửi link” để không ai gửi một nghìn mail cho người lạ. Response giống nhau dù email có tồn tại hay không, để không lộ tài khoản. Tôi log lần gửi và lần dùng, kèm ip, để hộp thư bị lấy vẫn nhìn thấy. Laravel Mail cộng signed URL làm được. Phần quan trọng là một lần, đã hash, sống ngắn, không phải tên helper.</p>""",
        "notes": "<p><strong>Know:</strong> Hash the token, short TTL, one-time, same response if the email is unknown.</p><p><strong>Trap:</strong> Storing the raw token, or a link that lasts a week.</p>",
    },
    {
        "id": "new-php-abuse",
        "page": "php",
        "section": "Common questions",
        "title": "Stop people abusing a public API",
        "hint": "Rate limit, cache, cheap queries. Not a captcha speech.",
        "q_en": "A public stats API is free. How do you stop people abusing it?",
        "a_en": """<p>Assume it will be scraped. I put a key even on a “free” API so I can revoke one client. I rate-limit by key and by ip, and I return 429 with a Retry-After. The handler is a cache of a precomputed number, not a live scan of the cases table on every anonymous hit. I page and I cap the window they can query. I log volume per key. If a key is clearly a bot I disable it. Auth and cost belong in the design, not in a later firewall ticket. I have not run an open API at internet scale. The same idea showed up on IELTS: untrusted clients, a tight endpoint, and the server as the source of truth.</p>""",
        "q_vi": "API thống kê public, miễn phí. Làm sao để không bị lạm dụng?",
        "a_vi": """<p>Giả định sẽ bị scrape. Tôi vẫn cấp key cho API “free” để thu hồi được một client. Rate-limit theo key và theo ip, trả 429 kèm Retry-After. Handler đọc cache một số đã tính sẵn, không quét bảng cases mỗi lần hit ẩn danh. Có phân trang và khống chế khoảng thời gian họ được hỏi. Tôi log sản lượng theo key. Key rõ là bot thì tắt. Auth và chi phí nằm trong thiết kế, không phải ticket firewall về sau. Tôi chưa chạy API mở ở quy mô internet. Cùng ý đó xuất hiện trên IELTS: client không tin được, endpoint hẹp, server là nguồn sự thật.</p>""",
        "notes": "<p><strong>Know:</strong> Key, rate limit, cache, cap the query, revoke.</p><p><strong>Trap:</strong> Running an unbounded GROUP BY on every public GET.</p>",
    },
    {
        "id": "new-php-artisan",
        "page": "php",
        "section": "Common questions",
        "title": "A six-hour Artisan command",
        "hint": "Chunk, queue, do not load the table into PHP.",
        "q_en": "An Artisan command reads MySQL and computes analytics. It takes six hours. Most steps do not depend on each other. How do you speed it up?",
        "a_en": """<p>First I ask whether SQL can do the aggregation. A <code>GROUP BY</code> in MySQL is faster than fetching every row into PHP. If the work is still per row and independent, I stop using one process. I chunk by id, I push many jobs onto a queue, and workers run them in parallel. Each job selects a range, only the columns it needs, and writes its result. I do not <code>Model::all()</code>. I do not wrap the whole six hours in one transaction. I make the job idempotent so a retry does not double-count. At Base, payroll export and sync jobs were this shape: chunk, queue, log the failures, do not hold the browser. I have not had a job that truly needed six hours after that treatment. If it still does, the next question is a warehouse or a replica, not a bigger PHP memory_limit.</p>""",
        "q_vi": "Một lệnh Artisan đọc MySQL và tính analytics, chạy sáu giờ. Hầu hết bước không phụ thuộc nhau. Làm sao cho nhanh?",
        "a_vi": """<p>Trước hết tôi hỏi SQL có làm được phần gộp không. <code>GROUP BY</code> trong MySQL nhanh hơn kéo từng dòng vào PHP. Nếu việc vẫn theo từng dòng và độc lập, tôi không dùng một process. Tôi cắt theo id, đẩy nhiều job vào queue, worker chạy song song. Mỗi job chọn một khoảng, chỉ cột cần, rồi ghi kết quả. Tôi không <code>Model::all()</code>. Tôi không bọc cả sáu giờ trong một transaction. Job phải idempotent để retry không đếm hai lần. Ở Base, export lương và job sync là hình dạng này: cắt nhỏ, queue, ghi lỗi, không giữ trình duyệt. Tôi chưa gặp job nào vẫn cần sáu giờ sau cách đó. Nếu vẫn cần, câu tiếp theo là warehouse hoặc replica, không phải memory_limit PHP to hơn.</p>""",
        "notes": "<p><strong>Know:</strong> SQL first, then chunked queue jobs, idempotent writes.</p><p><strong>Trap:</strong> Raising memory_limit and selecting the whole table.</p>",
    },
    {
        "id": "new-php-mutex",
        "page": "php",
        "section": "Common questions",
        "title": "What a mutex is, in PHP",
        "hint": "Share-nothing. Use a DB or Redis lock instead.",
        "q_en": "Explain what a mutex is, and why it is uncommon in PHP.",
        "a_en": """<p>A mutex is a lock so two threads do not enter the same critical section. In a typical PHP-FPM or Laravel queue setup, each request is its own process. A mutex inside one process does not stop the other workers. That is why you rarely see one in application PHP. When two jobs must not run the same partner export, I take a lock they can all see: <code>GET_LOCK</code> in MySQL, <code>SELECT … FOR UPDATE</code> on a row, or a Redis/cache lock with a TTL so a dead worker cannot hold it forever. <code>flock</code> is fine for one cron on one machine. It is not fine across two Cloud Run instances. PHP is share-nothing on purpose. Cross-process locks live in the database or in Redis, not in a static variable.</p>""",
        "q_vi": "Mutex là gì, và vì sao ít gặp trong PHP?",
        "a_vi": """<p>Mutex là khóa để hai thread không vào cùng một đoạn nguy hiểm. PHP-FPM hoặc queue Laravel thường mỗi request một process. Mutex trong một process không chặn worker khác. Vì vậy code ứng dụng PHP ít khi có mutex. Khi hai job không được chạy cùng một lần export đối tác, tôi lấy khóa cả hai đều thấy: <code>GET_LOCK</code> trong MySQL, <code>SELECT … FOR UPDATE</code> trên một dòng, hoặc lock Redis/cache có TTL để worker chết không giữ mãi. <code>flock</code> ổn cho một cron trên một máy. Không ổn trên hai instance Cloud Run. PHP cố ý share-nothing. Khóa xuyên process nằm ở database hoặc Redis, không nằm ở biến static.</p>""",
        "notes": "<p><strong>Know:</strong> PHP processes do not share memory. Lock in MySQL or Redis.</p><p><strong>Trap:</strong> A static $locked flag in a controller.</p>",
    },
    {
        "id": "new-php-search",
        "page": "php",
        "section": "Common questions",
        "title": "Fuzzy search on 50 million rows",
        "hint": "Honesty first. MySQL LIKE will not do 50–300ms.",
        "q_en": "You have 50 million rows in MySQL. How do you do fuzzy search and faceting in 50–300ms?",
        "a_en": """<p>Not with <code>LIKE '%qnap%'</code> on that table. A B-tree cannot help a leading wildcard, and faceting — counts per warehouse, per status, per product line — wants aggregations a primary MySQL node should not recompute on every keystroke. The usual architecture is a search engine next to MySQL: Elasticsearch, OpenSearch, or Meilisearch. MySQL stays the source of truth. A worker writes to the index when a row changes. The search box and the facet counts hit the engine. I have not operated 50 million rows. At Base the heavy tables were hundreds of thousands, and the fix was indexes, pagination, and not selecting columns we did not render. If this portal’s inventory search is thousands of SKUs, MySQL is enough. If they truly have tens of millions and type-ahead, I would say so, and I would not pretend I have already built that cluster.</p>""",
        "q_vi": "50 triệu dòng trong MySQL. Làm fuzzy search và facet trong 50–300ms thế nào?",
        "a_vi": """<p>Không phải bằng <code>LIKE '%qnap%'</code> trên bảng đó. B-tree không giúp ký tự <code>%</code> đứng đầu, và facet — đếm theo kho, theo trạng thái, theo dòng sản phẩm — là phép gộp mà node MySQL chính không nên tính lại mỗi lần gõ. Kiến trúc thường gặp là một search engine cạnh MySQL: Elasticsearch, OpenSearch, hoặc Meilisearch. MySQL vẫn là nguồn sự thật. Worker ghi vào index khi một dòng đổi. Ô tìm và số facet đánh vào engine. Tôi chưa vận hành 50 triệu dòng. Ở Base bảng nặng là hàng trăm nghìn, và cách sửa là index, phân trang, và không select cột không vẽ. Nếu ô tìm tồn kho của portal này là vài nghìn SKU, MySQL đủ. Nếu họ thật sự có hàng chục triệu và type-ahead, tôi sẽ nói vậy, và tôi không giả vờ đã dựng cluster đó.</p>""",
        "notes": "<p><strong>Know:</strong> Search engine beside MySQL. MySQL remains the source of truth.</p><p><strong>Trap:</strong> Claiming 50 million LIKE queries at 50ms.</p>",
    },
    {
        "id": "new-php-uptime",
        "page": "php",
        "section": "Common questions",
        "title": "High traffic and 99.9% uptime",
        "hint": "Shape, then honesty. You have not run millions of visitors.",
        "q_en": "How would you keep a high-traffic site up around 99.9% of the time, even if one server dies?",
        "a_en": """<p>I have not run millions of visitors a day. The shape I would start from is still simple. More than one app server behind a load balancer, so one box can die. The database is not on the web box. Health checks remove a bad instance. Sessions and uploads live in Redis or object storage, not on local disk. Hot reads can be cached. Writes and reports that take seconds leave the request and go to a queue. If the primary database dies, a replica can serve reads; failover of writes is a runbook, not a hope. 99.9% is about eight hours of downtime a year, so deploys and migrations have to be boring. I would measure error rate and latency before I buy a more exotic topology. At Akktis and on the tutor, Cloud Run already gave me more than one instance. I would not invent Kubernetes in the interview to sound senior.</p>""",
        "q_vi": "Giữ site traffic lớn quanh 99.9% uptime, kể cả khi một server chết, thế nào?",
        "a_vi": """<p>Tôi chưa chạy hàng triệu khách mỗi ngày. Hình dạng tôi bắt đầu vẫn đơn giản. Nhiều hơn một app server sau load balancer, để một máy chết được. Database không nằm trên máy web. Health check gỡ instance hỏng. Session và file upload nằm ở Redis hoặc object storage, không nằm đĩa local. Đọc nóng có thể cache. Ghi và report mất vài giây rời request, vào queue. Primary database chết thì replica phục vụ đọc; failover ghi là runbook, không phải hy vọng. 99.9% là khoảng tám giờ downtime một năm, nên deploy và migration phải nhàm chán. Tôi đo error rate và latency trước khi mua topology cầu kỳ hơn. Ở Akktis và trên tutor, Cloud Run đã cho tôi hơn một instance. Tôi không bịa Kubernetes trong interview để nghe như senior.</p>""",
        "notes": "<p><strong>Know:</strong> Redundant app, DB off the web box, cache, queue, boring deploys.</p><p><strong>Trap:</strong> Claiming an HA story you have not operated.</p>",
    },
    {
        "id": "new-php-queue",
        "page": "php",
        "section": "Common questions",
        "title": "Queue versus the HTTP request",
        "hint": "If the user should not wait, it is a job.",
        "q_en": "What belongs in the HTTP request, and what belongs on a queue?",
        "a_en": """<p>The request does the thing the user is staring at: validate, authorize, write the case, return the id. Mail, Excel export, partner notify, analytics, and sync with another system go on a queue. If it can take more than a second, or if it can fail and retry, it is a job. At Base, VSS sync and payroll export were jobs. A partner-application approval should commit the status in the request, then queue the email. I do not start a six-minute report inside <code>index()</code> and hope the proxy timeout is kind.</p>""",
        "q_vi": "Cái gì nằm trong HTTP request, cái gì nằm trên queue?",
        "a_vi": """<p>Request làm việc user đang nhìn: validate, authorize, ghi case, trả id. Mail, export Excel, báo đối tác, analytics, và đồng bộ hệ thống khác đi vào queue. Nếu có thể hơn một giây, hoặc có thể fail rồi retry, đó là job. Ở Base, sync VSS và export lương là job. Duyệt hồ sơ đối tác nên commit trạng thái trong request, rồi queue email. Tôi không mở report sáu phút trong <code>index()</code> rồi hy vọng timeout của proxy tử tế.</p>""",
        "notes": "<p><strong>Know:</strong> User-facing write in the request. Slow or retryable work on a queue.</p>",
    },
    {
        "id": "new-php-eloquent",
        "page": "php",
        "section": "Common questions",
        "title": "Eloquent versus the query builder",
        "hint": "Models for one record. SQL you can see for a report.",
        "q_en": "When do you use Eloquent, and when do you use the query builder?",
        "a_en": """<p>Eloquent is for one model and its relations: load a case, <code>with(['partner', 'warehouse'])</code>, update status, fire the usual events. A report that joins five tables, or a batch that must show me the SQL, I write with the query builder. I can paste that SQL into EXPLAIN. I use raw SQL only when the builder cannot say it, and I still bind the values. I do not put a 40-line query in a Blade file. I do not disable the query log in production and then guess.</p>""",
        "q_vi": "Khi nào dùng Eloquent, khi nào dùng query builder?",
        "a_vi": """<p>Eloquent cho một model và quan hệ của nó: load một case, <code>with(['partner', 'warehouse'])</code>, đổi trạng thái, bắn event bình thường. Report join năm bảng, hoặc batch mà tôi phải nhìn thấy SQL, tôi viết query builder. Tôi dán SQL đó vào EXPLAIN. Raw SQL chỉ khi builder không nói được, và tôi vẫn bind giá trị. Tôi không nhét query 40 dòng vào file Blade. Tôi không tắt query log trên production rồi đoán.</p>""",
        "notes": "<p><strong>Know:</strong> Eloquent for the unit of work. Builder when you need to see the SQL.</p><p><strong>Trap:</strong> Eloquent in a loop, which is N+1 with nicer syntax.</p>",
    },
]
