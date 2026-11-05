"""Full-stack interview prompts: SQL, Node, payments, email, React cache."""

EXTRA = [
    {
        "id": "new-sql-second-salary",
        "page": "php",
        "section": "SQL",
        "title": "Second-highest salary",
        "hint": "Say what 'second' means when two people share the top.",
        "q_en": "Write a query for the second-highest salary.",
        "a_en": """<p>I have run this shape on MySQL, not on a Postgres cluster. The SQL is the same idea. 'Second' has to mean the next distinct salary, or two people on the top salary make OFFSET 1 return the same number.</p>
<pre>SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;</pre>
<p>If they want everyone on the second tier, I use a rank:</p>
<pre>SELECT salary
FROM (
  SELECT salary,
         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 2;</pre>
<p>LIMIT and OFFSET work in MySQL and PostgreSQL. I would confirm NULL salaries are excluded, because NULL sorts first or last depending on the engine.</p>""",
        "q_vi": "Viết query lấy lương cao thứ hai.",
        "a_vi": """<p>Em đã chạy dạng này trên MySQL, chưa vận hành một cụm Postgres. SQL cùng một ý. 'Thứ hai' phải là mức lương khác tiếp theo, nếu không hai người cùng mức cao nhất khiến OFFSET 1 trả lại đúng số đó.</p>
<pre>SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;</pre>
<p>Nếu họ muốn mọi người ở bậc thứ hai, em dùng rank:</p>
<pre>SELECT salary
FROM (
  SELECT salary,
         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 2;</pre>
<p>LIMIT và OFFSET chạy được trên MySQL và PostgreSQL. Em sẽ hỏi lương NULL có bị loại không, vì NULL sắp đầu hoặc cuối tùy engine.</p>""",
        "notes": "<p><strong>Know:</strong> DISTINCT or DENSE_RANK. OFFSET 1 without DISTINCT can repeat the top salary.</p><p><strong>Trap:</strong> Claiming a Postgres-only career. You have operated MySQL.</p>",
    },
    {
        "id": "new-sql-update",
        "page": "php",
        "section": "SQL",
        "title": "Write an UPDATE",
        "hint": "SELECT the WHERE first. Then the transaction.",
        "q_en": "Write an update query. What do you check first?",
        "a_en": """<p>I write the WHERE as a SELECT and read the row count before I change anything. Then the same filter goes into the UPDATE, inside a transaction.</p>
<pre>BEGIN;
SELECT id, salary FROM employees
WHERE department_id = 4 AND salary &lt; 2000;

UPDATE employees
SET salary = salary * 1.1
WHERE department_id = 4 AND salary &lt; 2000;
COMMIT;</pre>
<p>No WHERE means every row. I do not run that. PostgreSQL can add <code>RETURNING id, salary</code> so I see what changed. MySQL I follow with a SELECT. On payroll data at Base, a wrong update is worse than a slow one, so the preview is the point.</p>""",
        "q_vi": "Viết một câu UPDATE. Bạn kiểm tra gì trước?",
        "a_vi": """<p>Em viết WHERE thành SELECT và xem số dòng trước khi sửa. Rồi đúng filter đó vào UPDATE, trong một transaction.</p>
<pre>BEGIN;
SELECT id, salary FROM employees
WHERE department_id = 4 AND salary &lt; 2000;

UPDATE employees
SET salary = salary * 1.1
WHERE department_id = 4 AND salary &lt; 2000;
COMMIT;</pre>
<p>Không có WHERE là sửa cả bảng. Em không chạy câu đó. PostgreSQL thêm được <code>RETURNING id, salary</code> để thấy dòng vừa đổi. MySQL thì em SELECT lại. Với dữ liệu lương ở Base, update sai tệ hơn update chậm, nên bước xem trước mới là điểm chính.</p>""",
        "notes": "<p><strong>Know:</strong> Preview, WHERE, transaction.</p><p><strong>Trap:</strong> UPDATE with no WHERE, then COMMIT.</p>",
    },
    {
        "id": "new-sql-dupes",
        "page": "php",
        "section": "SQL",
        "title": "Delete duplicate rows",
        "hint": "Keep one id per email. Then add a unique key.",
        "q_en": "Delete duplicate rows and leave one row per email.",
        "a_en": """<p>I decide which row survives. Usually the smallest id. A window makes that obvious in both PostgreSQL and MySQL 8:</p>
<pre>DELETE FROM employees
WHERE id IN (
  SELECT id FROM (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM employees
  ) ranked
  WHERE rn &gt; 1
);</pre>
<p>I run the inner SELECT first and read how many rows would go. After the delete I add <code>UNIQUE (email)</code>, or the duplicates come back on the next import. I do this in a transaction, and I do not delete from a table I have not backed up when the data is payroll.</p>""",
        "q_vi": "Xóa dòng trùng và giữ một dòng cho mỗi email.",
        "a_vi": """<p>Em chọn dòng nào được giữ. Thường là id nhỏ nhất. Window function nói rõ điều đó trên cả PostgreSQL và MySQL 8:</p>
<pre>DELETE FROM employees
WHERE id IN (
  SELECT id FROM (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM employees
  ) ranked
  WHERE rn &gt; 1
);</pre>
<p>Em chạy SELECT bên trong trước và xem bao nhiêu dòng sẽ mất. Xóa xong em thêm <code>UNIQUE (email)</code>, không thì lần import sau trùng lại. Làm trong transaction, và em không xóa bảng chưa backup khi data là lương.</p>""",
        "notes": "<p><strong>Know:</strong> ROW_NUMBER, keep one, then a unique constraint.</p><p><strong>Trap:</strong> DELETE the duplicates and leave the door open.</p>",
    },
    {
        "id": "new-node-slow",
        "page": "node",
        "section": "Common questions",
        "title": "An API is slow",
        "hint": "Name the layer before you add a cache.",
        "q_en": "An API takes too long. How do you troubleshoot it?",
        "a_en": """<p>I time the request before I change code. Three places eat the time. The database: turn on the query log, look for N+1 or a scan, run EXPLAIN. An outside call: the payment provider, or on IELTS the model, with no timeout. Our own CPU: a huge JSON body, or bcrypt on the login path blocking the event loop. I fix the one that the timing points at. A missing index on a Base report was that kind of bug. Caching a slow wrong query just makes the wrong answer faster.</p>""",
        "q_vi": "Một API trả lời quá lâu. Bạn điều tra thế nào?",
        "a_vi": """<p>Em đo request trước khi sửa code. Ba chỗ ngốn thời gian. Database: bật query log, tìm N+1 hoặc quét bảng, chạy EXPLAIN. Lời gọi ra ngoài: cổng thanh toán, hoặc trên IELTS là model, không có timeout. CPU của mình: body JSON khổng lồ, hoặc bcrypt trên đường login chặn event loop. Em sửa đúng chỗ timing chỉ. Thiếu index trên một report ở Base là kiểu bug đó. Cache một query chậm mà sai chỉ làm câu trả lời sai chạy nhanh hơn.</p>""",
        "notes": "<p><strong>Know:</strong> DB, outbound call, or CPU. One measurement, one change.</p><p><strong>Trap:</strong> Adding Redis before you know the layer.</p>",
    },
    {
        "id": "new-node-login-spike",
        "page": "node",
        "section": "Common questions",
        "title": "Thousands of logins at once",
        "hint": "You have not had this spike. Say the shape.",
        "q_en": "How would you handle thousands of simultaneous login requests?",
        "a_en": """<p>I have not had that spike. The shape I would use: the app is stateless, so a second instance can take load. Sessions live in Redis or a database, not in the memory of one Node process. The pool to that store is bounded. Password hashing is CPU, so it must not block the event loop. I rate-limit the login route and return 429 instead of letting the request sit for 30 seconds. Login is not a queue. The user is waiting. The closest thing I have operated is Cloud Run running more than one instance for the IELTS API.</p>""",
        "q_vi": "Hàng nghìn request đăng nhập cùng lúc thì xử lý thế nào?",
        "a_vi": """<p>Em chưa gặp mức spike đó. Hình dạng em sẽ dùng: app không giữ state, nên instance thứ hai nhận tải được. Session nằm ở Redis hoặc database, không nằm trong bộ nhớ một process Node. Pool tới kho đó có giới hạn. Hash mật khẩu là CPU, nên không được chặn event loop. Em rate-limit route login và trả 429 thay vì để request nằm 30 giây. Login không phải hàng đợi. User đang chờ. Thứ gần nhất em đã chạy là Cloud Run với hơn một instance cho API IELTS.</p>""",
        "notes": "<p><strong>Know:</strong> Stateless app, shared session store, async hash, 429.</p><p><strong>Trap:</strong> Claiming you have already survived this spike.</p>",
    },
    {
        "id": "new-node-secure",
        "page": "node",
        "section": "Common questions",
        "title": "How you secure an API",
        "hint": "A checklist you can say in order.",
        "q_en": "How do you secure an API?",
        "a_en": """<p>HTTPS. Then authentication, and then authorization on the record, not only a hidden button. I validate the body. SQL is parameterized. Secrets stay in the platform, not in git. Expensive or public routes are rate-limited. A payment or a webhook has an idempotency key so a retry is safe. Errors to the client are generic. CORS is not star in production. On IELTS the store notification is verified before we grant anything. On payroll data the same rule was: this user may see this row, or they may not.</p>""",
        "q_vi": "Bạn bảo vệ một API thế nào?",
        "a_vi": """<p>HTTPS. Rồi xác thực, rồi phân quyền trên đúng bản ghi, không chỉ giấu nút. Em validate body. SQL dùng tham số. Secret nằm trên nền tảng, không nằm trong git. Route đắt hoặc public thì rate-limit. Thanh toán hoặc webhook có idempotency key để retry an toàn. Lỗi trả client là lỗi chung. CORS không phải dấu sao trên production. Trên IELTS, thông báo từ store được verify trước khi cấp quyền. Với data lương, luật giống vậy: user này được xem dòng này, hoặc không.</p>""",
        "notes": "<p><strong>Know:</strong> Authn, authz, validation, secrets, rate limit, idempotency.</p><p>The longer Node security card is earlier on this page.</p>",
    },
    {
        "id": "new-node-deploy",
        "page": "node",
        "section": "Common questions",
        "title": "How you deploy Node",
        "hint": "CI, container, previous revision. Not git pull on a server.",
        "q_en": "Walk through deploying a Node API.",
        "a_en": """<p>A push runs CI. Tests pass, then the pipeline builds a container and deploys it. On IELTS that target is Cloud Run. Env and secrets are set on the service, not baked into the image. A health check has to pass. If the new revision is bad, I send traffic back to the previous revision. I do not SSH into a box and git pull. Akktis was the same idea on their pipeline. I would follow this team's script instead of inventing a new one.</p>""",
        "q_vi": "Kể quy trình deploy một API Node.",
        "a_vi": """<p>Một lần push chạy CI. Test qua, pipeline build container rồi deploy. Trên IELTS đích là Cloud Run. Env và secret đặt trên service, không nhét vào image. Health check phải qua. Revision mới hỏng thì em chuyển traffic về revision trước. Em không SSH vào máy rồi git pull. Akktis là cùng ý trên pipeline của họ. Em sẽ theo script của team này, không bịa một quy trình mới.</p>""",
        "notes": "<p><strong>Know:</strong> Test, image, platform secrets, rollback to the previous revision.</p>",
    },
    {
        "id": "new-system-shop",
        "page": "system",
        "section": "Common questions",
        "title": "E-commerce, modules first",
        "hint": "You have not run a microservice estate. Say that, then the boundaries.",
        "q_en": "Explain the services of an e-commerce platform.",
        "a_en": """<p>I have not operated a microservice platform. I would not start there with a small team. I would start with modules in one app: catalog, cart, order, payment, inventory. Split one out when it has its own traffic or its own team. If they already have services, the order service owns the order. Payment talks to the provider. Inventory reserves stock. The user-facing read, 'is this SKU available', can be a direct call. 'Order paid' is an event, so email and the warehouse do not sit inside the pay request. At Akktis I supported a live shop. At Base the same lesson was boundaries: payroll must not half-write because another system was slow.</p>""",
        "q_vi": "Kể các service của một sàn thương mại điện tử.",
        "a_vi": """<p>Em chưa vận hành một nền microservice. Em không bắt đầu từ đó với team nhỏ. Em bắt đầu bằng module trong một app: catalog, giỏ, đơn, thanh toán, tồn kho. Tách một phần ra khi nó có traffic riêng hoặc team riêng. Nếu họ đã có service, service đơn sở hữu đơn. Thanh toán nói với nhà cung cấp. Tồn kho giữ hàng. Câu user đang chờ, 'SKU này còn không', có thể là lời gọi thẳng. 'Đơn đã trả' là một event, để email và kho không nằm trong request thanh toán. Ở Akktis em hỗ trợ một shop đang chạy. Ở Base bài học giống vậy là ranh giới: lương không được ghi nửa chừng vì hệ thống khác chậm.</p>""",
        "notes": "<p><strong>Know:</strong> Modules until a boundary hurts. Sync for the waiting user, event after the fact.</p><p><strong>Trap:</strong> Drawing ten boxes you have never run.</p>",
    },
    {
        "id": "new-system-talk",
        "page": "system",
        "section": "Common questions",
        "title": "How services talk",
        "hint": "HTTP when they wait. A queue when the fact already happened.",
        "q_en": "How do services communicate?",
        "a_en": """<p>If the user is waiting, I use a direct call: HTTP, with a timeout. If the fact already happened, I publish an event and a queue delivers it. OrderPaid does not need the email server to answer before we show the receipt. The event has a version and an id. The consumer is idempotent, because the queue will retry. I have done this inside one codebase: payroll sync jobs, and Apple or Google notifications hitting Express twice. I have not run a bus across many repos. The rule is the same.</p>""",
        "q_vi": "Các service nói chuyện với nhau thế nào?",
        "a_vi": """<p>Nếu user đang chờ, em gọi thẳng: HTTP, có timeout. Nếu việc đã xảy ra, em phát một event và queue chuyển nó. OrderPaid không cần server email trả lời trước khi hiện biên lai. Event có version và id. Consumer phải idempotent, vì queue sẽ thử lại. Em đã làm kiểu này trong một codebase: job sync lương, và thông báo Apple hoặc Google đập vào Express hai lần. Em chưa chạy một bus qua nhiều repo. Luật thì giống nhau.</p>""",
        "notes": "<p><strong>Know:</strong> Sync plus timeout, or async plus an idempotent consumer.</p>",
    },
    {
        "id": "new-system-email",
        "page": "system",
        "section": "Common questions",
        "title": "Email one million people",
        "hint": "A campaign row and a queue. Not a for-loop in the request.",
        "q_en": "How would you send a promotion to one million users?",
        "a_en": """<p>Not in the HTTP request. I write one campaign row, then chunks of user ids onto a queue. Workers call an email provider. The provider's rate limit is the bottleneck, not our loop. Each chunk records sent and failed. I have sent mail from background jobs. I have not sent one million. The shape is the payroll export: chunk, queue, keep the failures, do not hold the browser.</p>""",
        "q_vi": "Gửi khuyến mãi cho một triệu user thế nào?",
        "a_vi": """<p>Không nằm trong HTTP request. Em ghi một dòng campaign, rồi từng cụm id user vào queue. Worker gọi nhà cung cấp email. Giới hạn tốc độ của nhà cung cấp mới là nút thắt, không phải vòng lặp của mình. Mỗi cụm ghi đã gửi và gửi lỗi. Em đã gửi mail từ job nền. Em chưa gửi một triệu. Hình dạng là export lương: cắt nhỏ, queue, giữ phần lỗi, không giữ trình duyệt.</p>""",
        "notes": "<p><strong>Know:</strong> Campaign, chunks, provider, a record of failures.</p><p><strong>Trap:</strong> Awaiting a million SMTP calls inside the controller.</p>",
    },
    {
        "id": "new-system-email-fast",
        "page": "system",
        "section": "Common questions",
        "title": "Those emails in one or two minutes",
        "hint": "Do the math. The provider decides.",
        "q_en": "What if those million emails must be processed in one or two minutes?",
        "a_en": """<p>One million in two minutes is about eight thousand a second. A normal SMTP loop will not do that. I would ask what the provider's batch API allows, then run many workers on many chunks. What we can promise in two minutes is: the campaign is accepted, every recipient is queued, and the screen shows progress. Inbox delivery follows the provider. I would not promise that a million people have the mail in two minutes. I have not run this volume.</p>""",
        "q_vi": "Nếu một triệu email đó phải xử lý trong một hoặc hai phút?",
        "a_vi": """<p>Một triệu trong hai phút là khoảng tám nghìn mỗi giây. Vòng SMTP thường không làm được. Em sẽ hỏi batch API của nhà cung cấp cho phép bao nhiêu, rồi chạy nhiều worker trên nhiều cụm. Thứ em hứa được trong hai phút là: campaign được nhận, mọi người nhận đã vào hàng đợi, và màn hình hiện tiến độ. Tới hộp thư thì theo nhà cung cấp. Em không hứa một triệu người có mail trong hai phút. Em chưa chạy khối lượng này.</p>""",
        "notes": "<p><strong>Know:</strong> Say the number. Queue acceptance is not inbox delivery.</p>",
    },
    {
        "id": "new-system-email-status",
        "page": "system",
        "section": "Common questions",
        "title": "Track whether the email arrived",
        "hint": "The provider webhook is the source of truth.",
        "q_en": "How do you track email delivery in the database?",
        "a_en": """<p>One row per message: user, campaign, our id, the provider's id, and a status. We insert it as queued. The provider later calls a webhook: sent, delivered, bounced, complaint. That handler updates the row and is idempotent on the provider event id, because they retry. The user's browser is not the source of truth. This is the same shape as an Apple purchase notification: the outside system tells us what happened, and a unique id stops a double write.</p>""",
        "q_vi": "Theo dõi email đã tới chưa, trong database, thế nào?",
        "a_vi": """<p>Một dòng cho mỗi thư: user, campaign, id của mình, id của nhà cung cấp, và trạng thái. Lúc tạo thì queued. Sau đó nhà cung cấp gọi webhook: sent, delivered, bounced, complaint. Handler cập nhật dòng và idempotent theo event id của họ, vì họ gửi lại. Trình duyệt của user không phải nguồn sự thật. Cùng hình dạng với thông báo mua của Apple: hệ ngoài báo chuyện đã xảy ra, và id duy nhất chặn ghi hai lần.</p>""",
        "notes": "<p><strong>Know:</strong> A status row plus an idempotent webhook.</p>",
    },
    {
        "id": "new-system-double-pay",
        "page": "system",
        "section": "Common questions",
        "title": "The Pay button clicked twice",
        "hint": "A unique key. Hiding the button is not the fix.",
        "q_en": "The user clicks Pay twice. How do you prevent two charges?",
        "a_en": """<p>Disabling the button is only the screen. The API takes an idempotency key, or we use the provider's payment id, and that column is unique. The second request finds the row and returns it. It does not create another charge. I have lived the cousin of this bug: Apple and Google send the same purchase notification twice, and the unique store transaction id is what stops a second grant. I would test with two parallel requests.</p>""",
        "q_vi": "User bấm Pay hai lần. Làm sao không bị trừ tiền hai lần?",
        "a_vi": """<p>Tắt nút chỉ là màn hình. API nhận một idempotency key, hoặc dùng payment id của nhà cung cấp, và cột đó unique. Request thứ hai thấy dòng và trả lại dòng đó. Nó không tạo lần trừ tiền nữa. Em đã gặp anh em của bug này: Apple và Google gửi cùng một thông báo mua hai lần, và transaction id duy nhất của store là thứ chặn lần cấp quyền thứ hai. Em sẽ test bằng hai request song song.</p>""",
        "notes": "<p><strong>Know:</strong> Unique idempotency key. The button is not the lock.</p><p>The API version of this answer is on the PHP page.</p>",
    },
    {
        "id": "new-system-pay-mismatch",
        "page": "system",
        "section": "Common questions",
        "title": "Provider charged, our write failed",
        "hint": "The webhook is the source of truth. Then a reconcile job.",
        "q_en": "The payment provider succeeds, then our backend fails. What now?",
        "a_en": """<p>I do not trust the browser redirect. The provider webhook, or a reconcile job, decides that the payment exists. We store their payment id as unique. If our insert died after they charged the card, their retry hits that unique key and becomes one row. If the webhook never arrived, a job lists their payments since yesterday and inserts the ones we are missing. I do not refund because I am unsure. On IELTS a repeated store notification was the same class of problem: the outside system is the record, and we catch up.</p>""",
        "q_vi": "Nhà cung cấp đã trừ tiền, rồi backend mình lỗi. Lúc đó sao?",
        "a_vi": """<p>Em không tin redirect trên trình duyệt. Webhook của nhà cung cấp, hoặc một job đối soát, mới quyết định khoản thanh toán tồn tại. Mình lưu payment id của họ dạng unique. Nếu insert của mình chết sau khi họ đã trừ thẻ, lần retry của họ đụng unique key và thành một dòng. Nếu webhook không bao giờ tới, một job liệt kê payment của họ từ hôm qua và thêm những khoản mình thiếu. Em không hoàn tiền vì em không chắc. Trên IELTS, thông báo store bị lặp là cùng loại: hệ ngoài là hồ sơ, mình bắt kịp.</p>""",
        "notes": "<p><strong>Know:</strong> Unique provider id, webhook retry, reconcile. No guess-refund.</p>",
    },
    {
        "id": "new-react-optimize",
        "page": "react",
        "section": "Common questions",
        "title": "Optimize a React component",
        "hint": "Measure. Then data, keys, and memo.",
        "q_en": "How do you optimize a React component?",
        "a_en": """<p>I look at why it is slow before I wrap it in memo. A long list is usually too much data: paginate, or virtualize. Keys stay stable. A parent that builds a new function or a new object every render will wake a memoized child, so that is when useCallback or useMemo earns its place. I do not memo every component. A heavy screen can be code-split. On the IELTS app the win was not loading every topic for one practice screen. I would profile, change one thing, and check again.</p>""",
        "q_vi": "Bạn tối ưu một component React thế nào?",
        "a_vi": """<p>Em xem vì sao nó chậm trước khi bọc memo. List dài thường là quá nhiều data: phân trang, hoặc virtualize. Key giữ ổn định. Parent tạo function mới hoặc object mới mỗi lần render sẽ đánh thức child đã memo, lúc đó useCallback hoặc useMemo mới đáng. Em không memo mọi component. Màn nặng thì tách code. Trên app IELTS, phần thắng là không tải mọi topic cho một màn luyện. Em sẽ đo, đổi một thứ, rồi kiểm lại.</p>""",
        "notes": "<p><strong>Know:</strong> Less data, stable keys, memo only at a real boundary.</p><p><strong>Trap:</strong> useMemo on every value.</p>",
    },
    {
        "id": "new-react-stale",
        "page": "react",
        "section": "Common questions",
        "title": "Users still see old data after deploy",
        "hint": "Two caches: index.html, and the API.",
        "q_en": "You deployed frontend and backend. Users still see old data. What do you check?",
        "a_en": """<p>Two different caches. The JavaScript: hashed files can be cached for a long time, but index.html must not be, or the browser keeps the old bundle. I look at the Network tab, disable cache, and read Cache-Control on index.html. A service worker can pin the old app too. The API is the other cache: CDN, Cache-Control, or a client cache that still holds the previous JSON. I compare the response with the database. If the response is new and the screen is old, it is the client. If the response is old, it is the server or the CDN. I have hit stale bundles. I do not tell the user to 'clear cache' until I know which cache.</p>""",
        "q_vi": "Đã deploy frontend và backend. User vẫn thấy data cũ. Bạn kiểm tra gì?",
        "a_vi": """<p>Hai cache khác nhau. JavaScript: file có hash thì cache lâu được, nhưng index.html thì không, nếu không trình duyệt giữ bundle cũ. Em xem tab Network, tắt cache, và đọc Cache-Control của index.html. Service worker cũng có thể ghim app cũ. API là cache kia: CDN, Cache-Control, hoặc cache phía client còn giữ JSON lần trước. Em so response với database. Response mới mà màn hình cũ thì là client. Response cũ thì là server hoặc CDN. Em đã gặp bundle cũ. Em không bảo user 'xóa cache' trước khi biết cache nào.</p>""",
        "notes": "<p><strong>Know:</strong> index.html versus hashed assets, then the API cache.</p><p><strong>Trap:</strong> One 'clear your cache' reply for both bugs.</p>",
    },
]
