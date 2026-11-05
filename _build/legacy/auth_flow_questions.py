"""Auth, one request, and notifications — with a flow you can look at."""

GOOGLE_FLOW = """
<div class="flow" role="img" aria-label="Sign in with Google">
<div class="flow-box"><span>1</span><strong>App</strong><p>User taps Sign in with Google. Your app is the client. It never sees the Google password.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>Google</strong><p>User agrees. Google returns a one-time code, or an id token. Google is the authorization server.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>Your API</strong><p>Verify that token with Google. Create or find the user in your database.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>Your API</strong><p>Return your own session or JWT. From here, later calls do not go back to Google.</p></div>
</div>
<p class="flow-note">OAuth 2.0 is this handshake. JWT is only one shape of the token in step 4.</p>
"""

GOOGLE_FLOW_VI = """
<div class="flow" role="img" aria-label="Đăng nhập bằng Google">
<div class="flow-box"><span>1</span><strong>App</strong><p>User bấm Sign in with Google. App của mình là client. Nó không bao giờ thấy mật khẩu Google.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>Google</strong><p>User đồng ý. Google trả một code dùng một lần, hoặc một id token. Google là authorization server.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>API của mình</strong><p>Verify token đó với Google. Tạo hoặc tìm user trong database.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>API của mình</strong><p>Trả session hoặc JWT của mình. Từ đây, các lần gọi sau không quay lại Google.</p></div>
</div>
<p class="flow-note">OAuth 2.0 là cái bắt tay này. JWT chỉ là một hình dạng token ở bước 4.</p>
"""

JWT_FLOW = """
<div class="flow" role="img" aria-label="A later API call with a JWT">
<div class="flow-box"><span>1</span><strong>App</strong><p>Sends <code>Authorization: Bearer &lt;jwt&gt;</code>. The JWT has three parts: header.payload.signature.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>API</strong><p>Check the signature with your secret or public key. If it is wrong, 401. Do not trust the payload yet.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>API</strong><p>Read <code>sub</code> and <code>exp</code>. Expired is 401. Then authorize this user on this row.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>API</strong><p>Handler runs. JWT said who. Your code still says what they may do.</p></div>
</div>
"""

JWT_FLOW_VI = """
<div class="flow" role="img" aria-label="Một lần gọi API sau đó với JWT">
<div class="flow-box"><span>1</span><strong>App</strong><p>Gửi <code>Authorization: Bearer &lt;jwt&gt;</code>. JWT có ba phần: header.payload.signature.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>API</strong><p>Kiểm chữ ký bằng secret hoặc public key. Sai thì 401. Chưa tin payload.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>API</strong><p>Đọc <code>sub</code> và <code>exp</code>. Hết hạn thì 401. Rồi phân quyền user này trên đúng dòng này.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>API</strong><p>Handler chạy. JWT nói là ai. Code của mình mới nói họ được làm gì.</p></div>
</div>
"""

SERVER_FLOW = """
<div class="flow" role="img" aria-label="One HTTP request through Node">
<div class="flow-box"><span>1</span><strong>Client</strong><p>Phone or browser sends HTTPS. The user is waiting.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>Process</strong><p>Cloud Run or a Node process accepts the socket. One JavaScript thread. I/O can wait. CPU cannot.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>Middleware</strong><p>Parse JSON. Auth. A request id for logs. If auth fails, stop. Do not enter the business layer.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>Route → service → DB</strong><p>The handler calls one service. The service talks to MySQL or Firestore. Await the I/O.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>5</span><strong>Response</strong><p>JSON back, or an error middleware that does not leak the stack. Long work goes on a queue, not here.</p></div>
</div>
"""

SERVER_FLOW_VI = """
<div class="flow" role="img" aria-label="Một HTTP request đi qua Node">
<div class="flow-box"><span>1</span><strong>Client</strong><p>Điện thoại hoặc trình duyệt gửi HTTPS. User đang chờ.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>Process</strong><p>Cloud Run hoặc một process Node nhận socket. Một thread JavaScript. I/O có thể chờ. CPU thì không.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>Middleware</strong><p>Parse JSON. Auth. Một request id để log. Auth fail thì dừng. Không vào tầng nghiệp vụ.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>Route → service → DB</strong><p>Handler gọi một service. Service nói với MySQL hoặc Firestore. Await I/O.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>5</span><strong>Response</strong><p>JSON trả về, hoặc error middleware không leak stack. Việc dài nằm trên queue, không nằm đây.</p></div>
</div>
"""

NOTIFY_FLOW = """
<div class="flow" role="img" aria-label="In-app row, then a push if the phone is closed">
<div class="flow-box"><span>1</span><strong>Event</strong><p>A reminder is due, or a clinic message arrives. Your API writes a notification row: user, title, read = false.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>In-app</strong><p>The next time the app opens, it lists unread rows. That is enough if they are already inside the product.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>Push, if needed</strong><p>If the phone is closed, send to FCM or APNs with a stored device token. The OS shows the banner. Your server does not draw the banner.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>Tap</strong><p>The app opens the right screen. Mark the row read. A retry from FCM must not create a second row.</p></div>
</div>
<p class="flow-note">A local notification is only on the phone. No server. That is the IELTS practice reminder.</p>
"""

NOTIFY_FLOW_VI = """
<div class="flow" role="img" aria-label="Một dòng in-app, rồi push nếu điện thoại đang tắt">
<div class="flow-box"><span>1</span><strong>Sự kiện</strong><p>Tới giờ nhắc, hoặc có tin từ phòng khám. API ghi một dòng notification: user, tiêu đề, read = false.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>2</span><strong>Trong app</strong><p>Lần mở app tới, nó liệt kê dòng chưa đọc. Đủ nếu họ đang ở trong sản phẩm.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>3</span><strong>Push, nếu cần</strong><p>Nếu điện thoại đang tắt, gửi FCM hoặc APNs với device token đã lưu. OS hiện banner. Server không vẽ banner.</p></div>
<div class="flow-arrow" aria-hidden="true">↓</div>
<div class="flow-box"><span>4</span><strong>Bấm</strong><p>App mở đúng màn. Đánh dấu đã đọc. Retry từ FCM không được tạo dòng thứ hai.</p></div>
</div>
<p class="flow-note">Local notification chỉ nằm trên điện thoại. Không có server. Đó là lời nhắc luyện trên IELTS.</p>
"""

EXTRA = [
    {
        "id": "new-auth-oauth",
        "page": "node",
        "section": "How it works",
        "title": "OAuth, OAuth 2, and JWT",
        "hint": "Three names. Two jobs. Look at the Google path.",
        "q_en": "What is the difference between OAuth, OAuth 2, and JWT?",
        "a_en": f"""<p>They are not three ways to do the same thing.</p>
<table class="compare">
<thead><tr><th></th><th>What it is</th><th>What you say</th></tr></thead>
<tbody>
<tr><td><strong>OAuth 1</strong></td><td>Old protocol. Every request is signed.</td><td>I would not start a new app on this.</td></tr>
<tr><td><strong>OAuth 2</strong></td><td>A handshake. Your app asks Google (or Apple) to prove who the user is, without the password.</td><td>Sign in with Google is this.</td></tr>
<tr><td><strong>JWT</strong></td><td>A token format: header.payload.signature. Anyone can read the payload. Only your key proves it is yours.</td><td>Often the thing you hand out after OAuth 2 succeeds.</td></tr>
</tbody>
</table>
{GOOGLE_FLOW}
<p>On IELTS I am the client, not Google. Express verifies the Google id token or the Apple identity token, then creates the user. Later API calls on that app use a simple identity header, not a JWT on every route. Apple IAP is a JWS we verify. I would not claim I run an OAuth 2 authorization server.</p>""",
        "q_vi": "OAuth, OAuth 2, và JWT khác nhau thế nào?",
        "a_vi": f"""<p>Không phải ba cách làm cùng một việc.</p>
<table class="compare">
<thead><tr><th></th><th>Nó là gì</th><th>Câu nói</th></tr></thead>
<tbody>
<tr><td><strong>OAuth 1</strong></td><td>Protocol cũ. Mỗi request đều được ký.</td><td>Em không bắt đầu app mới bằng cái này.</td></tr>
<tr><td><strong>OAuth 2</strong></td><td>Một cái bắt tay. App nhờ Google (hoặc Apple) chứng minh user là ai, không lấy mật khẩu.</td><td>Sign in with Google là cái này.</td></tr>
<tr><td><strong>JWT</strong></td><td>Một định dạng token: header.payload.signature. Ai cũng đọc được payload. Chỉ key của mình chứng minh là của mình.</td><td>Thường là thứ mình đưa ra sau khi OAuth 2 xong.</td></tr>
</tbody>
</table>
{GOOGLE_FLOW_VI}
<p>Trên IELTS em là client, không phải Google. Express verify id token của Google hoặc identity token của Apple, rồi tạo user. Các lần gọi API sau trên app đó dùng một header định danh đơn giản, không phải JWT trên mọi route. IAP của Apple là JWS mình verify. Em không nhận là em đang chạy một authorization server OAuth 2.</p>""",
        "notes": "<p><strong>Know:</strong> OAuth 2 = handshake. JWT = token format.</p><p><strong>Trap:</strong> “We use OAuth JWT” with no picture. Also do not claim the IELTS API is JWT on every route.</p>",
    },
    {
        "id": "new-auth-jwt",
        "page": "node",
        "section": "How it works",
        "title": "How you check a JWT",
        "hint": "Signature first. Then expiry. Then the row.",
        "q_en": "A client sends a JWT. What does the server do?",
        "a_en": f"""<p>A JWT is three base64 pieces joined by dots. The middle is JSON anyone can decode. The last piece is the signature. If I skip the signature check, anyone can send <code>admin: true</code>.</p>
{JWT_FLOW}
<p>Access tokens stay short. A refresh token lives in httpOnly cookie or secure storage, and I rotate it. Logout means I revoke the refresh id in the database. You cannot kill a JWT that is already out in the wild except by waiting for <code>exp</code> or keeping a denylist. I still check this user may see this record. The token is not permission.</p>
<p>The longer “JWT versus session” answer, and what IELTS actually sends, is earlier on this page.</p>""",
        "q_vi": "Client gửi một JWT. Server làm gì?",
        "a_vi": f"""<p>JWT là ba khúc base64 nối bằng dấu chấm. Khúc giữa là JSON ai cũng decode được. Khúc cuối là chữ ký. Nếu em bỏ qua chữ ký, ai cũng gửi <code>admin: true</code> được.</p>
{JWT_FLOW_VI}
<p>Access token để ngắn. Refresh token nằm trong cookie httpOnly hoặc kho an toàn, và em xoay nó. Logout nghĩa là revoke refresh id trong database. JWT đã phát ra ngoài thì không giết được, trừ khi chờ <code>exp</code> hoặc giữ denylist. Em vẫn kiểm user này được xem bản ghi này. Token không phải quyền.</p>
<p>Câu “JWT versus session” dài hơn, và IELTS thực tế gửi gì, nằm ở phần trước trên trang này.</p>""",
        "notes": "<p><strong>Know:</strong> Verify signature, then exp, then authz.</p><p><strong>Trap:</strong> Decoding the payload and trusting it.</p>",
    },
    {
        "id": "new-server-request",
        "page": "node",
        "section": "How it works",
        "title": "How the server handles one request",
        "hint": "One thread. I/O waits. CPU must not.",
        "q_en": "Walk through what happens when a request hits your Node API.",
        "a_en": f"""<p>The user is waiting, so this path stays short.</p>
{SERVER_FLOW}
<p>If two of these arrive at once, Node is not two threads of JavaScript. It starts the first, hits <code>await db.query</code>, and can start the second while MySQL works. That is the event loop. bcrypt on the login path, or a huge JSON transform, blocks everyone. Those go off the request. I have run this on Express on Cloud Run. A 500k-row report in PHP taught me the same rule: do not do it in the request.</p>""",
        "q_vi": "Kể chuyện gì xảy ra khi một request đập vào API Node.",
        "a_vi": f"""<p>User đang chờ, nên path này để ngắn.</p>
{SERVER_FLOW_VI}
<p>Nếu hai request tới cùng lúc, Node không phải hai thread JavaScript. Nó bắt đầu cái một, gặp <code>await db.query</code>, và có thể bắt đầu cái hai khi MySQL đang làm. Đó là event loop. bcrypt trên đường login, hoặc transform JSON khổng lồ, chặn mọi người. Những cái đó ra khỏi request. Em đã chạy vậy trên Express trên Cloud Run. Report 500k dòng trong PHP dạy cùng một luật: đừng làm trong request.</p>""",
        "notes": "<p>The event-loop card and the middleware card are earlier on this page. This one is the picture.</p>",
    },
    {
        "id": "new-notify-push",
        "page": "node",
        "section": "How it works",
        "title": "How you send a notification",
        "hint": "A row first. Push only if the phone is closed.",
        "q_en": "How would you implement notifications?",
        "a_en": f"""<p>Three different things share the word.</p>
{NOTIFY_FLOW}
<p>What I have shipped: local reminders on the IELTS app, scheduled on the phone, and mail or store webhooks from the server. I have not run FCM or APNs for a clinic product. If INTOWELL needs a consult alert while the app is closed, I would store the device token at login, send through their existing provider, and keep the in-app row as the source of truth. Email is the same shape with a different provider.</p>""",
        "q_vi": "Bạn implement notification thế nào?",
        "a_vi": f"""<p>Ba thứ khác nhau dùng chung một chữ.</p>
{NOTIFY_FLOW_VI}
<p>Cái em đã ship: lời nhắc local trên app IELTS, lên lịch trên điện thoại, và mail hoặc webhook store từ server. Em chưa chạy FCM hoặc APNs cho một sản phẩm phòng khám. Nếu INTOWELL cần báo tư vấn khi app đang tắt, em sẽ lưu device token lúc login, gửi qua nhà cung cấp họ đang dùng, và giữ dòng in-app là nguồn sự thật. Email là cùng hình với nhà cung cấp khác.</p>""",
        "notes": "<p><strong>Know:</strong> Row, then optional push, then idempotent tap.</p><p><strong>Trap:</strong> Claiming you ran FCM because the JD has a mobile app.</p>",
    },
]
