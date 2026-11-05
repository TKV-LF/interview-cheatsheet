#!/usr/bin/env python3
"""Insert a Node.js backend section into engineering.html (JD: Node fullstack)."""
from __future__ import annotations

import html as H
import re
import sys
from pathlib import Path

ROOT = Path("/Users/thuynt/Working/Vibe/interview-cheatsheet")
ENG = ROOT / "engineering.html"
sys.path.insert(0, str(ROOT / "_build"))

from html_lib import p_html  # noqa: E402


def esc(s: str) -> str:
    return H.escape(s or "", quote=False)


def card(cid: str, num: int, title: str, sub: str, q_en: str, a_en: str, q_vi: str, a_vi: str,
         know: str, trap: str = "", follow: str = "") -> tuple[str, str, str]:
    crib = [f"<p><strong>Know:</strong> {esc(know)}</p>"]
    if trap:
        crib.append(f"<p><strong>Trap:</strong> {esc(trap)}</p>")
    if follow:
        crib.append(f"<p><strong>Follow-up:</strong> {esc(follow)}</p>")
    html = f"""<article class="question-card" id="{esc(cid)}">
        <div class="question-head"><h2>{num:02d}. {esc(title)}</h2><p>{esc(sub)}</p></div>
        <div class="grid4">
          <div class="cell row-head">Question EN</div><div class="cell row-head">Answer EN</div>
          <div class="cell row-head">Question VI</div><div class="cell row-head">Answer VI</div>
          <div class="cell question">{p_html(q_en)}</div>
          <div class="cell answer">{p_html(a_en)}</div>
          <div class="cell question">{p_html(q_vi)}</div>
          <div class="cell answer">{p_html(a_vi)}</div>
        </div>
        <div class="crib">
          {"".join(crib)}
        </div>
      </article>"""
    return cid, title, html


CARDS = [
    card(
        "n1", 1, "Node.js backend experience (honest)",
        "Lead with IELTS Express. PHP/MySQL is still the deepest SQL backend. Nest is a ramp.",
        "What's your Node.js backend experience?",
        "The Node product I can walk through is IELTS AI Tutor. I built the React Native/TypeScript app on iOS and Android, and the backend is Express on Cloud Run — auth, practice content, AI tutor, TTS/STT, study plans, in-app purchase webhooks, user progress, and a teacher assignment portal. That's a real Express API in production, not a tutorial. My deepest SQL and enterprise APIs are still PHP/MySQL at BaseVN — 500k-row reporting, sync jobs. I have not owned a Nest estate. For a Node role I lead with this Express product plus those PHP API habits.",
        "Kinh nghiệm Node.js backend của bạn?",
        "Sản phẩm Node tôi đi được end-to-end là IELTS AI Tutor. Tôi làm app React Native/TypeScript trên iOS và Android, backend là Express trên Cloud Run — auth, nội dung luyện tập, AI tutor, TTS/STT, study plan, webhook IAP, tiến độ user, và portal giáo viên. Đó là Express production thật, không phải tutorial. API SQL/enterprise sâu nhất vẫn là PHP/MySQL ở BaseVN — report 500k row, job sync. Tôi chưa own hệ Nest. Với role Node tôi dẫn bằng sản phẩm Express này cộng thói quen PHP API.",
        "IELTS = Express on Cloud Run · RN client · PHP/MySQL still deepest SQL · no Nest estate",
        "Saying 'senior Nest' or hiding that IELTS already runs Express.",
        "Walk me through one Express route you shipped on IELTS.",
    ),
    card(
        "n2", 2, "Event loop and async",
        "Must-know Node interview.",
        "How does the Node.js event loop work, and why does it matter?",
        "Node is single-threaded for JavaScript. CPU-heavy work blocks the loop; I/O like DB, HTTP, and files is offloaded and comes back as callbacks or promises. That is why async/await is the default for APIs: don't block while waiting for MySQL or a third-party HTTP call. I treat long CPU work — big JSON transform, heavy image processing — as a job or a worker, not inside the request. Same idea I already use in PHP: don't do a 500k-row report inside the user request.",
        "Event loop Node.js hoạt động thế nào, vì sao quan trọng?",
        "Node chạy JavaScript một thread. Việc nặng CPU chặn loop; I/O như DB, HTTP, file được offload rồi callback/promise. Vì thế API mặc định dùng async/await: đừng block khi chờ MySQL hoặc HTTP bên thứ ba. Việc CPU dài — transform JSON lớn, xử lý ảnh nặng — tôi để job/worker, không nhét trong request. Cùng ý tôi đã dùng ở PHP: không làm report 500k row trong request của user.",
        "Single thread · I/O async · CPU work off the request",
        "await in a tight CPU loop and calling it 'scale'.",
        "What happens if you run a 2-second CPU loop in a route?",
    ),
    card(
        "n3", 3, "Express vs Nest vs raw http",
        "Awareness + how you'd choose.",
        "When would you use Express, Nest, or Node's http module?",
        "Raw http is fine for a tiny health check, not for a product API. Express is thin: you assemble middleware, routes, and your own structure — fast to start, easy to make messy. Nest gives modules, DI, and a place for controllers vs services — better when the team wants structure, TypeScript, and test seams. On IELTS I used Express with one router file per domain — TTS, agent, IAP, storage, study plan — because the product grew as APIs, not as a Nest rewrite. I pick what the team already runs. I can work Express immediately; Nest I ramp from the same module habits I use in PHP/Laravel.",
        "Khi nào dùng Express, Nest, hoặc http module của Node?",
        "http thuần ổn cho health check nhỏ, không phải API sản phẩm. Express mỏng: tự ghép middleware, route, structure — start nhanh, dễ rối. Nest có module, DI, chỗ cho controller vs service — hợp khi team muốn structure, TypeScript, và test. Ở IELTS tôi dùng Express, mỗi domain một router — TTS, agent, IAP, storage, study plan — vì product lớn theo API, không rewrite sang Nest. Tôi chọn cái team đang chạy. Express tôi làm được ngay; Nest tôi ramp từ thói quen module đã dùng ở PHP/Laravel.",
        "Express = IELTS production · Nest = structured TS ramp · follow the team",
        "Rewriting their Nest app to Express in week one.",
        "How is a Nest guard different from Express middleware?",
    ),
    card(
        "n4", 4, "Design a Node API",
        "JD: write effective APIs.",
        "How do you design a backend API in Node.js?",
        "I start from the client use case — React or React Native — then freeze the contract: URL, method, auth, request/response JSON, error shape. Validation at the edge. Controllers stay thin; business rules in services; DB access in a repository or query module. Status codes mean something: 400 validation, 401/403 auth, 404 missing, 409 conflict, 5xx we failed. I keep APIs boring and version when we break clients. Same discipline I used on PHP APIs for enterprise SaaS.",
        "Bạn thiết kế API Node.js thế nào?",
        "Tôi bắt đầu từ use case client — React hoặc React Native — rồi chốt contract: URL, method, auth, JSON request/response, shape lỗi. Validation ở mép. Controller mỏng; business rule ở service; DB ở repository hoặc module query. Status code có nghĩa: 400 validation, 401/403 auth, 404 thiếu, 409 conflict, 5xx mình lỗi. API nhàm chán và version khi phá client. Cùng discipline tôi dùng trên PHP API cho SaaS enterprise.",
        "Contract-first · thin controller · predictable errors",
        "Fat routes with SQL and business rules mixed.",
        "How do you version an API without breaking the mobile app?",
    ),
    card(
        "n5", 5, "Middleware and request lifecycle",
        "How a Node request actually runs.",
        "Walk me through a request in Express or Nest.",
        "Request hits the server → parser (JSON) → auth/session middleware → logging/correlation id → route handler → service → DB → response. Errors go to an error middleware so we don't leak stack traces. In Nest that is pipes, guards, interceptors, then the controller. I care that secrets never log, and that a failed auth does not continue into the business layer.",
        "Đi qua một request trong Express hoặc Nest.",
        "Request vào server → parser JSON → middleware auth/session → log/correlation id → route → service → DB → response. Lỗi đi vào error middleware để không leak stack. Nest thì pipe, guard, interceptor, rồi controller. Tôi quan tâm secret không vào log, và auth fail thì không chạy tiếp vào business layer.",
        "Parse → auth → handler → error boundary",
        "Catching errors only inside one route and ignoring the rest.",
        "Where would you put rate limiting?",
    ),
    card(
        "n6", 6, "Client-side vs server-side architecture",
        "JD: design client-side and server-side architecture.",
        "How do you split client-side and server-side architecture?",
        "The client owns UI state, routing, and how the screen feels — React/React Native, responsive layout. The server owns truth: authz, validation, business rules, persistence, and anything secret. I don't put prices, permissions, or 'is admin' only in the frontend. APIs are the contract. If a feature needs a background job — export, sync, email — that stays server-side so a closed laptop doesn't kill it. I draw the boundary early with the PM: what the user sees vs what must be correct even if someone tampers with the client.",
        "Bạn tách kiến trúc client và server thế nào?",
        "Client own UI state, routing, cảm giác màn hình — React/React Native, layout responsive. Server own sự thật: authz, validation, business rule, persistence, và mọi thứ secret. Tôi không để giá, quyền, hay 'is admin' chỉ ở frontend. API là contract. Feature cần job nền — export, sync, email — để server, laptop tắt không được giết việc. Tôi vẽ ranh giới sớm với PM: user thấy gì vs cái phải đúng dù ai đó sửa client.",
        "UI on client · truth and secrets on server · API is the contract",
        "Hiding a button as authorization.",
        "What must never live only in React state?",
    ),
    card(
        "n7", 7, "Work with PMs to ideate",
        "JD: work with development teams and product managers.",
        "How do you work with product managers to ideate a solution?",
        "I ask for the user outcome and the constraint — deadline, existing mobile app, what data we already have. Then I propose a thin vertical slice: one API + one screen that proves the idea, not a six-month platform. I name risks early: third-party API, data quality, auth. I write the contract in plain language so FE, BE, and PM share the same picture. If scope grows, I say what drops this sprint so quality doesn't collapse.",
        "Bạn làm việc với PM để ideate giải pháp thế nào?",
        "Tôi hỏi outcome của user và ràng buộc — deadline, app mobile sẵn, data đã có. Rồi đề xuất slice dọc mỏng: một API + một màn hình chứng minh ý tưởng, không phải platform sáu tháng. Tôi nêu risk sớm: API bên thứ ba, chất lượng data, auth. Viết contract bằng lời thường để FE, BE và PM cùng một bức tranh. Nếu scope phình, tôi nói sprint này bỏ gì để chất lượng không sụp.",
        "Outcome · thin slice · risks · shared contract",
        "Jumping to architecture before the user problem is clear.",
        "Give an example of a slice you shipped with a PM.",
    ),
    card(
        "n8", 8, "MySQL from Node",
        "JD: databases (MySQL). This is your strong side.",
        "How do you work with MySQL from a Node API?",
        "Same rules as PHP: parameterized queries, indexes, watch N+1, don't hide a report in the request. In Node I'd use a query builder or ORM the team already has — knex, Prisma, TypeORM — but I still want to see the SQL for slow paths. Connection pooling matters more in Node because many concurrent requests share the process. I have real MySQL experience at scale from BaseVN reporting and sync, including 500k+ row datasets. The language changes; the query plan does not.",
        "Bạn làm MySQL từ API Node thế nào?",
        "Cùng rule với PHP: query parameterized, index, tránh N+1, đừng nhét report vào request. Node tôi dùng query builder hoặc ORM team đang có — knex, Prisma, TypeORM — nhưng path chậm tôi vẫn muốn thấy SQL. Connection pool quan trọng hơn vì nhiều request chung một process. Tôi có MySQL thật ở scale từ report/sync BaseVN, gồm dataset 500k+ row. Đổi ngôn ngữ; query plan không đổi.",
        "Parameterized SQL · indexes · pool · you've done this in PHP at scale",
        "String-concatenating SQL in JavaScript.",
        "How do you find a slow query from a Node service?",
    ),
    card(
        "n9", 9, "MongoDB familiarity",
        "JD lists MongoDB. Be honest.",
        "What's your experience with MongoDB?",
        "My production SQL is MySQL at BaseVN. On IELTS the document store is Firestore, not Mongo — user progress, entitlements, classes and assignments live as documents keyed by user. I understand the document model: nested, per-user, query by document, not HR-style joins. Mongo is the same idea with a different engine. I would not claim I operated a Mongo cluster. If this team uses Mongo, I ramp from that Firestore/document habit plus MySQL for when related records must stay consistent.",
        "Kinh nghiệm MongoDB của bạn?",
        "SQL production của tôi là MySQL ở BaseVN. Ở IELTS document store là Firestore, không phải Mongo — tiến độ, entitlement, class/assignment là document theo user. Tôi hiểu model document: lồng, theo user, query theo document, không phải join kiểu HR. Mongo cùng ý với engine khác. Tôi không claim đã operate cluster Mongo. Nếu team dùng Mongo, tôi ramp từ thói quen Firestore/document cộng MySQL khi bản ghi liên quan phải consistent.",
        "MySQL = BaseVN · Firestore documents on IELTS · Mongo = same idea, not a cluster I ran",
        "Saying NoSQL is always faster, or claiming Mongo because the JD lists it.",
        "When is Mongo a bad fit?",
    ),
    card(
        "n10", 10, "OOP and design patterns",
        "JD: extensive knowledge of OOP and design patterns.",
        "How do you use OOP and design patterns in a Node/TypeScript backend?",
        "I use classes and interfaces in TypeScript the same way I do in PHP: a service owns a use case, a repository hides SQL, DTOs describe the API shape. Patterns I actually reach for: repository, strategy or a simple map for 'this vendor vs that vendor', factory for creating a client from config, and middleware as a pipeline. I don't force a pattern for a 20-line script. SOLID for me means: one reason to change, depend on interfaces at the edges — DB, email, payment — so tests can fake them. Nest's modules/providers are that idea with more ceremony.",
        "Bạn dùng OOP và design pattern trong Node/TypeScript backend thế nào?",
        "Tôi dùng class và interface TypeScript như PHP: service own use case, repository giấu SQL, DTO mô tả shape API. Pattern tôi thực sự dùng: repository, strategy hoặc map đơn giản cho 'vendor này vs vendor kia', factory tạo client từ config, và middleware như pipeline. Không nhồi pattern cho script 20 dòng. SOLID với tôi: một lý do để đổi, phụ thuộc interface ở mép — DB, email, payment — để test fake được. Module/provider của Nest là ý đó với nhiều ceremony hơn.",
        "Service + repository · strategy at integrations · SOLID at boundaries",
        "Name-dropping 12 patterns with no example from your work.",
        "Give a pattern you used on a BaseVN integration.",
    ),
    card(
        "n11", 11, "Test Node software",
        "JD: test for responsiveness and efficiency.",
        "How do you test a Node API?",
        "I test the risky contract: validation, authz, and the money/data path. Unit tests for pure functions and services with a fake repository. HTTP-level tests for status codes and JSON shape. I don't chase 100% coverage. For efficiency I add a slow-query log or a test that a list endpoint doesn't N+1. Same rule as PHP: protect the paths that hurt users if they break.",
        "Bạn test API Node thế nào?",
        "Tôi test contract rủi ro: validation, authz, và đường tiền/data. Unit cho hàm thuần và service với repository giả. Test HTTP cho status và shape JSON. Không đuổi 100% coverage. Hiệu năng thì slow-query log hoặc test list endpoint không N+1. Cùng rule PHP: bảo vệ path làm đau user nếu gãy.",
        "Contract tests · fake DB at the repository · N+1 check on lists",
        "Only manual Postman and calling it a test strategy.",
        "What would you test on a pagination endpoint?",
    ),
    card(
        "n12", 12, "Security and data protection",
        "JD: create security and data protection settings.",
        "How do you handle security and data protection in a Node app?",
        "HTTPS at the edge, secrets in env or a secret manager — never in Git. Helmet/CORS configured on purpose, not 'allow *' in production. Hash passwords, parameterized queries, validate file uploads. Authorization on every record, not only login. For personal or payroll-like data I minimize what we store, restrict who can query it, and audit access when the product needs it. I already think this way on PHP/HR/tax systems.",
        "Bạn xử lý bảo mật và bảo vệ dữ liệu trong app Node thế nào?",
        "HTTPS ở mép, secret trong env hoặc secret manager — không bao giờ trong Git. Helmet/CORS cấu hình có chủ đích, không 'allow *' trên production. Hash password, query parameterized, validate file upload. Authorization trên từng bản ghi, không chỉ login. Data kiểu personal/payroll tôi giảm thứ lưu, hạn chế ai query được, và audit khi product cần. Tôi đã nghĩ vậy trên hệ PHP/HR/thuế.",
        "Secrets out of Git · authz per record · CORS/Helmet on purpose",
        "CORS * plus secrets in the frontend bundle.",
        "How do you store an API key for a third-party service?",
    ),
    card(
        "n13", 13, "Auth: JWT vs session",
        "Mobile + web clients.",
        "How would you authenticate a React web app and a mobile app against Node?",
        "On IELTS the mobile client signs in with Google or Apple. The Express server verifies the Google id token or OAuth code, or Apple's identity token, then creates/updates the user. Later API calls send an X-Username header — that's a simple identity header, not a full JWT session on every route. IAP is different: Apple sends JWS, we verify the certificate chain. Web can use httpOnly cookies. JWT is a tool: short access, rotate refresh, revoke on logout. I still authorize on the server. I don't pretend X-Username is bank-grade auth — I'd tighten it toward signed tokens if the threat model needs it.",
        "Bạn authenticate app React web và mobile với Node thế nào?",
        "Ở IELTS client mobile đăng nhập Google hoặc Apple. Express verify Google id token hoặc OAuth code, hoặc identity token của Apple, rồi tạo/cập nhật user. API sau đó gửi header X-Username — identity đơn giản, không phải JWT session trên mọi route. IAP khác: Apple gửi JWS, mình verify chuỗi certificate. Web có thể cookie httpOnly. JWT là tool: access ngắn, rotate refresh, revoke lúc logout. Vẫn authorize trên server. Tôi không giả X-Username là auth ngân hàng — sẽ siết sang token ký nếu threat model cần.",
        "IELTS: Google/Apple verify on server · X-Username on APIs · JWT/JWS for IAP · honest about simple header",
        "Claiming JWT everywhere when the app uses a username header.",
        "How do you revoke a JWT before it expires?",
    ),
    card(
        "n14", 14, "Troubleshoot, debug, upgrade",
        "JD: troubleshoot, debug and upgrade software.",
        "A Node API is slow or throwing 5xx. What do you do?",
        "Reproduce, then split layers: is Node itself hot CPU, waiting on MySQL, or waiting on a third-party HTTP call? Logs with a request id, then timing. If it started after a deploy, I compare versions and env. Upgrade is separate: read the changelog, run tests, ship to staging, then production with a rollback. I don't jump Node major versions on Friday without a reason. Same incident habit I use on Cloud Run and PHP: evidence first, then a small safe change.",
        "API Node chậm hoặc 5xx. Bạn làm gì?",
        "Reproduce, rồi tách tầng: Node đang nóng CPU, chờ MySQL, hay chờ HTTP bên thứ ba? Log có request id, rồi timing. Nếu sau deploy, tôi so version và env. Upgrade là việc khác: đọc changelog, chạy test, staging, rồi production có rollback. Không nhảy major Node vào Friday không lý do. Cùng thói quen incident trên Cloud Run và PHP: evidence trước, rồi change nhỏ an toàn.",
        "Reproduce · isolate I/O vs CPU · changelog before upgrade",
        "Restarting the process as the only fix.",
        "How do you debug an async hang that never throws?",
    ),
    card(
        "n15", 15, "Web servers and running Node",
        "JD: familiarity with web servers.",
        "How do you run a Node API in production?",
        "Node listens on an internal port. A reverse proxy — Nginx or a cloud load balancer / Cloud Run — terminates TLS and forwards. I don't expose the Node process to the public internet if I can avoid it. Process manager or a container keeps it alive. I've operated Apache, LiteSpeed, and Cloud Run for real apps, so the pattern is familiar: proxy, TLS, logs, health check, rollback. On Cloud Run the 'web server' is the platform in front of the container.",
        "Bạn chạy API Node trên production thế nào?",
        "Node listen cổng nội bộ. Reverse proxy — Nginx hoặc load balancer / Cloud Run — terminate TLS rồi forward. Tôi không expose process Node ra internet nếu tránh được. Process manager hoặc container giữ nó sống. Tôi đã operate Apache, LiteSpeed và Cloud Run cho app thật, nên pattern quen: proxy, TLS, log, health check, rollback. Cloud Run thì 'web server' là platform phía trước container.",
        "Node behind TLS proxy · health · I've run Apache/LiteSpeed/Cloud Run",
        "Serving the API on :3000 with no TLS in production.",
        "Why put Nginx in front of Node?",
    ),
    card(
        "n16", 16, "TypeScript on the server",
        "You already write TS on the client.",
        "Why use TypeScript for a Node backend?",
        "Types catch contract mistakes before runtime — the same reason I use TypeScript in React Native. On IELTS the mobile client is TypeScript; the Express API is JavaScript with route modules. That split is honest: I ship TS where the UI contract lives, and I can work JS on the server. If the team is TS-first on Node, I'd type request bodies, DB rows, and response DTOs so client and API don't drift. I don't fight the compiler with any everywhere.",
        "Vì sao dùng TypeScript cho Node backend?",
        "Type bắt lỗi contract trước runtime — cùng lý do tôi dùng TypeScript trên React Native. Ở IELTS client mobile là TypeScript; API Express là JavaScript chia theo router. Đó là sự thật: tôi ship TS chỗ UI contract, và làm được JS phía server. Nếu team Node-first dùng TS, tôi type body request, row DB, DTO response để client và API không lệch. Không đánh compiler bằng any everywhere.",
        "RN client is TS · IELTS Express is JS · type the server if the team is TS-first",
        "any on every parameter and calling it TypeScript.",
        "How do you share types between a React app and a Node API?",
    ),
    card(
        "n17", 17, "Desktop and mobile applications",
        "JD: experience developing desktop and mobile. Stay honest.",
        "Have you developed desktop and mobile applications?",
        "Mobile: yes — IELTS AI Tutor is Expo / React Native / TypeScript, live on Google Play and the App Store. Feature modules: skills practice, study plan, IAP, AdMob gates, Google/Apple sign-in. The app talks to the Express API I maintain on Cloud Run. Desktop: I build web apps in the browser, including the teacher assignment portal and responsive layouts. I have not shipped a large Electron or native Windows desktop product. If desktop is a webview or responsive web, that is my path.",
        "Bạn đã làm ứng dụng desktop và mobile chưa?",
        "Mobile: có — IELTS AI Tutor là Expo / React Native / TypeScript, live Google Play và App Store. Module: luyện skill, study plan, IAP, cổng AdMob, đăng nhập Google/Apple. App nói chuyện với API Express tôi maintain trên Cloud Run. Desktop: web app trên browser, gồm portal giáo viên và layout responsive. Tôi chưa ship Electron hoặc Windows native lớn. Nếu desktop là webview hoặc web responsive, đó là path của tôi.",
        "Expo RN on both stores · portal = web · not Electron",
        "Equating 'I use VS Code' with desktop app experience.",
        "How does the mobile app authenticate to your API?",
    ),
    card(
        "n18", 18, "Technical documentation",
        "JD: write technical documentation.",
        "What technical docs do you actually write?",
        "I write the docs that save the next person: API contract, how to run locally, env vars, and the weird production gotcha. For a Node service that is README + OpenAPI or a short endpoint list, plus a runbook for deploy/rollback. I don't write a novel. I update the doc in the same PR as the behavior change so it doesn't rot.",
        "Bạn viết docs kỹ thuật nào?",
        "Tôi viết docs cứu người sau: contract API, cách chạy local, env var, và gotcha production lạ. Service Node thì README + OpenAPI hoặc list endpoint ngắn, cộng runbook deploy/rollback. Không viết tiểu thuyết. Tôi update doc trong cùng PR với behavior để không mục.",
        "Contract · local run · env · runbook in the same PR",
        "Docs in a wiki nobody updates.",
        "Show me the minimum README for a new Node service.",
    ),
    card(
        "n19", 19, "Common fullstack stack for this JD",
        "JD: familiarity with common stacks.",
        "What stack would you use for this fullstack role?",
        "A practical default: React + TypeScript on the client, Node API, MySQL for core business data, Redis later if we need cache or jobs, Nginx or Cloud Run in front. Mobile via React Native talking to the same API. What I already ship: IELTS is RN + Express + Firestore + Cloud Run; BaseVN/Akktis is PHP + MySQL. Mongo or Firestore when the product is document-shaped. Node is not a new shape — I already operate this.",
        "Bạn dùng stack nào cho role fullstack này?",
        "Mặc định thực tế: React + TypeScript phía client, API Node, MySQL cho data nghiệp vụ, Redis sau nếu cần cache hoặc job, Nginx hoặc Cloud Run phía trước. Mobile qua React Native gọi cùng API. Cái tôi đã ship: IELTS là RN + Express + Firestore + Cloud Run; BaseVN/Akktis là PHP + MySQL. Mongo hoặc Firestore khi product hình document. Node không phải shape mới — tôi đã operate cái này.",
        "IELTS: RN + Express + Firestore + Cloud Run · BaseVN: PHP + MySQL",
        "Inventing Kafka + k8s if the product is a CRUD app.",
        "Where would you put file uploads in that stack?",
    ),
    card(
        "n20", 20, "Responsive UI + efficient APIs",
        "JD: mobile responsive design + responsiveness/efficiency.",
        "How do you keep the product responsive on mobile and efficient on the server?",
        "On the client I build mobile-first layouts — I already ship RN and responsive web. On the API I return only the fields the screen needs, paginate lists, and index the query behind the list. I don't send a 500k-row dump to a phone. If the UI feels slow I check Network first: fat payload vs slow SQL vs chatty N+1 endpoints. Then I fix the layer that is lying.",
        "Bạn giữ product responsive trên mobile và hiệu quả phía server thế nào?",
        "Phía client tôi làm layout mobile-first — đã ship RN và web responsive. Phía API tôi trả field màn hình cần, paginate list, và index query phía sau list. Không gửi dump 500k row xuống điện thoại. Nếu UI chậm tôi xem Network trước: payload béo vs SQL chậm vs endpoint N+1. Rồi sửa đúng tầng đang nói dối.",
        "Mobile-first UI · paginate · index · Network tells you which layer",
        "Fixing CSS when the API returns 8MB of JSON.",
        "How would you design a mobile list that might have 100k rows in MySQL?",
    ),
    card(
        "n21", 21, "IELTS: what I actually shipped",
        "CV story. Mobile + Express, not 'I only did UI'.",
        "Walk me through the IELTS AI Tutor stack you built.",
        "It's a learning product: students practice IELTS on the phone, teachers assign work from a portal. I own the Expo React Native app — skills, study plan, IAP, ads, Google/Apple login — and I work on the Express API it calls. That API runs on Cloud Run. Practice JSON and listening audio live on the server; progress hydrates from Firestore into AsyncStorage so the topic list is not one HTTP call per item. AI tutor, TTS, STT, writing and speaking scores, and purchase webhooks are server routes. Live on Play Store and App Store.",
        "Đi qua stack IELTS AI Tutor bạn đã làm.",
        "Đây là sản phẩm học: học viên luyện IELTS trên điện thoại, giáo viên giao bài từ portal. Tôi own app Expo React Native — skill, study plan, IAP, ads, login Google/Apple — và làm API Express mà app gọi. API chạy Cloud Run. JSON luyện tập và audio listening ở server; tiến độ hydrate từ Firestore vào AsyncStorage nên list topic không phải một HTTP mỗi item. AI tutor, TTS, STT, chấm writing/speaking, webhook mua hàng là route server. Đã lên Play Store và App Store.",
        "RN client · Express on Cloud Run · Firestore progress · AI + IAP on the server",
        "Saying you only wrapped OpenAI in the app with no backend.",
        "What lives on the phone vs what must stay on the server?",
    ),
    card(
        "n22", 22, "IELTS Express API map",
        "JD: write APIs. Name real modules.",
        "How is the IELTS Node API structured?",
        "server.js is the Express entry: CORS, JSON parser, then route modules under src/api. Public: Google/Apple auth, IAP webhooks, some audio. Authenticated: TTS, transcribe, agent, practice, translation, storage, study-plan, writing assess, speaking, words, assignment-portal, feature flags. Auth middleware checks an X-Username header before those routes. Tracing boots first so Langfuse sees OpenAI calls. I add a feature by a new router file and app.use — not one giant server.js. Same idea as PHP controllers, just Express.",
        "API Node của IELTS được cấu trúc thế nào?",
        "server.js là entry Express: CORS, parser JSON, rồi router trong src/api. Public: auth Google/Apple, webhook IAP, một phần audio. Cần auth: TTS, transcribe, agent, practice, translation, storage, study-plan, chấm writing, speaking, words, assignment-portal, feature flag. Middleware kiểm header X-Username trước các route đó. Tracing bật trước để Langfuse thấy lệnh OpenAI. Feature mới là file router rồi app.use — không nhét hết vào server.js. Cùng ý controller PHP, chỉ là Express.",
        "One router per domain · auth on most /api · tracing before routes",
        "Memorizing every path. Name 4–5 domains, then go deep on one.",
        "Which routes must stay public, and why?",
    ),
    card(
        "n23", 23, "IELTS auth: Google, Apple, header",
        "Real flow. Don't upgrade it to JWT-everywhere.",
        "How does the IELTS app authenticate to the Node API?",
        "Sign-in is Google or Apple on the device. Express verifies the Google token or authorization code with google-auth-library, or Apple's identity token, then upserts the user in Firebase. After that the API client sends X-Username. That's identity, not a signed session on every call — I'd say so in an interview. Purchases are stricter: Apple JWS verified with the cert chain, Google Play via service account. Admin portal uses its own cookie/session. If they ask how I'd harden it: signed tokens with expiry, still authorize per resource.",
        "App IELTS authenticate với API Node thế nào?",
        "Đăng nhập Google hoặc Apple trên máy. Express verify token/code Google bằng google-auth-library, hoặc identity token Apple, rồi upsert user trên Firebase. Sau đó API client gửi X-Username. Đó là identity, chưa phải session ký trên mọi call — tôi nói thẳng. Mua hàng chặt hơn: JWS Apple verify chuỗi cert, Google Play qua service account. Portal admin có cookie/session riêng. Nếu hỏi cách siết: token ký có hạn, vẫn authorize theo resource.",
        "OAuth verify on server · X-Username is simple · IAP uses real crypto",
        "Calling the username header 'OAuth' or 'JWT'.",
        "Why can't IAP webhooks use the same auth as the mobile app?",
    ),
    card(
        "n24", 24, "Progress storage: hydrate, don't N+1",
        "JD: efficient APIs + client/server split.",
        "How do you store user progress between the app and the server?",
        "Server is the source of truth in Firestore under user_data/{username}. On app open or after Google/Apple sign-in the client calls GET /api/storage and writes every key into AsyncStorage. After that, reading a skill topic is local — we don't fan out GET /storage/key/:key per topic. Writes still go to the server and update the cache. That was a product bug we fixed: opening a skill used to look like N+1 HTTP. Same efficiency rule as BaseVN reports — don't hide a chatty loop in the UI.",
        "Bạn lưu tiến độ user giữa app và server thế nào?",
        "Server là nguồn thật trên Firestore user_data/{username}. Lúc mở app hoặc sau login Google/Apple, client gọi GET /api/storage rồi ghi hết key vào AsyncStorage. Sau đó đọc topic skill là local — không quạt GET /storage/key/:key từng topic. Ghi vẫn lên server và cập nhật cache. Đó là bug product đã sửa: mở skill từng giống N+1 HTTP. Cùng rule hiệu năng với report BaseVN — đừng giấu vòng lặp chatty trong UI.",
        "Hydrate once · AsyncStorage cache · writes still server-side",
        "Claiming the phone is the source of truth.",
        "What happens if hydrate fails on a flaky network?",
    ),
    card(
        "n25", 25, "AI on the server: agent, TTS, STT",
        "Product integration, not training models.",
        "How do the IELTS AI features work across mobile and Node?",
        "The phone never holds the OpenAI key. Chat goes to /api/agent: Express loads skill-specific prompts, prunes TTS audio out of history so tokens don't explode, and calls OpenAI with Langfuse wrapping. Speak-the-answer is POST /api/tts, audio file back. Speech-to-text hits /api/transcribe. Writing uses four band prompts — achievement, coherence, lexical, grammar. I observe with OpenTelemetry into Langfuse so a weird answer is a trace, not a guess. I integrate models into workflows; I don't train them.",
        "Tính năng AI IELTS chạy xuyên mobile và Node thế nào?",
        "Điện thoại không giữ key OpenAI. Chat vào /api/agent: Express load prompt theo skill, cắt audio TTS khỏi history để đỡ phình token, gọi OpenAI bọc Langfuse. Đọc câu trả lời là POST /api/tts, trả file audio. Nói thành chữ vào /api/transcribe. Writing dùng bốn prompt band — achievement, coherence, lexical, grammar. Quan sát bằng OpenTelemetry vào Langfuse nên câu lạ là trace, không đoán. Tôi gắn model vào workflow; không train model.",
        "Keys on server · prompts as files · Langfuse on OpenAI · prune audio from chat history",
        "Saying you built the LLM.",
        "How do you debug a bad tutor answer in production?",
    ),
    card(
        "n26", 26, "IAP: Apple and Google on Express",
        "Money path. Server must be source of truth.",
        "How do in-app purchases work on IELTS?",
        "The mobile app talks to the store. Entitlement is not 'the client says Pro'. Express has /api/iap: verify purchase, store entitlements and transactions in Firestore, Slack a human when money moves. Apple webhooks send JWS — we verify alg and x5c, not trust the payload blindly. Google uses Play APIs with a service account. Offer signing is authenticated. Webhooks stay public with a shared secret because Apple/Google call us, not the user. Ads and daily quotas on the client respect that Pro flag from the server.",
        "In-app purchase trên IELTS hoạt động thế nào?",
        "App nói chuyện với store. Entitlement không phải 'client bảo là Pro'. Express có /api/iap: verify purchase, lưu entitlement và transaction trên Firestore, Slack người khi có tiền. Webhook Apple gửi JWS — mình verify alg và x5c, không tin payload mù. Google dùng Play API với service account. Ký offer cần user đã login. Webhook để public kèm secret vì Apple/Google gọi mình, không phải user. Ads và quota trên client tôn trọng cờ Pro từ server.",
        "Verify on server · Firestore entitlements · webhook ≠ user JWT",
        "Unlocking Pro only in AsyncStorage.",
        "What do you do if a webhook arrives twice?",
    ),
    card(
        "n27", 27, "Teacher portal + mobile: two clients",
        "JD: client/server architecture.",
        "How do the teacher portal and the student app share one backend?",
        "One Express API, two clients. Teachers hit assignment-portal routes: classes, assignments, quizsets, submissions in Firestore. Students open the same assignment from the mobile app by submission id. Auth still goes through the user in the request. I don't duplicate business rules in the portal HTML and the RN screens — the server owns 'this submission belongs to this class'. Cloud Run is the glue. If the contract breaks, both clients break, so I change API and clients in one slice.",
        "Portal giáo viên và app học viên chia backend thế nào?",
        "Một API Express, hai client. Giáo viên gọi route assignment-portal: class, assignment, quizset, submission trên Firestore. Học viên mở cùng assignment từ app bằng submission id. Auth vẫn đi qua user trong request. Tôi không nhân đôi rule trong HTML portal và màn RN — server own 'submission này thuộc class này'. Cloud Run là keo. Contract gãy thì cả hai client gãy, nên đổi API và client trong một slice.",
        "Two clients · one contract · server owns assignment truth",
        "Syncing by copying JSON files between apps.",
        "What if the teacher edits an assignment the student already started?",
    ),
    card(
        "n28", 28, "Study plan and writing/speaking scores",
        "LLM as a structured API, not a chatbot dump.",
        "How does the study-plan or scoring API stay reliable?",
        "Study plan is POST to Express: exam date, current bands, then the model must return JSON that matches a schema — weeks, skills, topic ids — not a free essay. Writing assess loads markdown prompts per IELTS criterion and scores the answer. Speaking has its own assessment plus grounding so feedback stays on the transcript. If the model drifts, Langfuse shows the prompt and output. I treat the LLM like a flaky third-party: validate shape, timeout, fail visible. Same instinct as E-Hiring job-board APIs.",
        "API study-plan hoặc chấm điểm giữ độ tin cậy thế nào?",
        "Study plan là POST lên Express: ngày thi, band hiện tại, model phải trả JSON đúng schema — tuần, skill, topic id — không phải bài văn. Chấm writing load prompt markdown theo tiêu chí IELTS rồi chấm. Speaking có assess riêng plus grounding để feedback dính transcript. Model lệch thì Langfuse hiện prompt và output. Tôi coi LLM như API bên thứ ba hay fail: validate shape, timeout, lỗi phải thấy. Cùng instinct với API job-board E-Hiring.",
        "JSON schema on plans · prompt files per band · traces when output is weird",
        "Pasting model output into the UI with no validation.",
        "What happens when the model returns a topic id that does not exist?",
    ),
    card(
        "n29", 29, "Firestore on IELTS vs MySQL at BaseVN",
        "Pick the store from the product, not the JD buzzword.",
        "Why Firestore on IELTS if you are strong at MySQL?",
        "IELTS progress is per-user documents — topic keys, settings, entitlements — not payroll joins. Firestore fits that; Cloud Run talks through firebase-admin. Base PIT and VSS needed MySQL: related tables, 500k rows, Excel/XML, transactions. I don't force Firestore onto tax data or MySQL onto a phone's nested progress blob. For a Node JD that lists MySQL, I bring BaseVN. For documents, I bring IELTS. Mongo would be the middle cousin of Firestore, not something I operated as a cluster.",
        "Vì sao IELTS dùng Firestore trong khi bạn mạnh MySQL?",
        "Tiến độ IELTS là document theo user — key topic, setting, entitlement — không phải join payroll. Firestore hợp; Cloud Run nói qua firebase-admin. Base PIT và VSS cần MySQL: bảng liên quan, 500k row, Excel/XML, transaction. Không nhét Firestore vào data thuế hay MySQL vào blob tiến độ trên điện thoại. JD liệt MySQL thì tôi mang BaseVN. Document thì mang IELTS. Mongo là họ hàng của Firestore, không phải cluster tôi đã operate.",
        "Document store for app state · MySQL for related business records",
        "Saying Firestore and MySQL are interchangeable.",
        "Would you migrate IELTS progress to MySQL? When yes / no?",
    ),
    card(
        "n30", 30, "React Native app architecture",
        "What you built on the phone.",
        "How is the IELTS mobile app organized?",
        "Expo Router, TypeScript, feature folders: auth, skills, practice, studyPlan, home, settings. Shared API client sends identity headers. Auth context hydrates storage after login. Ads live in core/ads — rewarded gates for study-plan rebuild and writing/speaking limits; Pro users skip banners. IAP client talks to store then /api/iap. Local notifications for practice reminders. I test scoring and storage helpers with Jest. Store builds go through EAS / CI, then Play and App Store — that's the same release muscle on the DevOps page.",
        "App mobile IELTS được tổ chức thế nào?",
        "Expo Router, TypeScript, folder theo feature: auth, skills, practice, studyPlan, home, settings. API client chung gửi header identity. Auth context hydrate storage sau login. Ads trong core/ads — cổng rewarded cho rebuild study-plan và hạn writing/speaking; user Pro không thấy banner. Client IAP nói store rồi /api/iap. Notification local nhắc luyện. Tôi test helper chấm điểm và storage bằng Jest. Build store qua EAS/CI, rồi Play và App Store — cùng cơ release ở trang DevOps.",
        "Feature modules · hydrate after auth · ads/IAP respect server Pro · Jest on scoring",
        "Calling it 'a few screens wrapping ChatGPT'.",
        "How do you keep a practice session usable offline after hydrate?",
    ),
]


def toc_and_section() -> tuple[str, str, str]:
    toc = ['<!-- NODE-BACKEND-TOC -->',
           '        <div class="side-toc-part" data-part="sec-node">',
           '          <a class="side-toc-part-link" href="#sec-node">Node.js backend</a>',
           f'          <span class="side-toc-part-range">{len(CARDS)} Q</span>',
           "        </div>"]
    articles = []
    for i, (cid, title, html) in enumerate(CARDS, start=1):
        toc.append(
            f'        <a class="side-toc-link" href="#{cid}" data-target="{cid}" data-part="sec-node">'
            f'<span class="side-toc-num">N{i:02d}</span>'
            f'<span class="side-toc-title">{esc(title)}</span></a>'
        )
        articles.append(html)
    toc.append("        <!-- /NODE-BACKEND-TOC -->")
    section = (
        "<!-- NODE-BACKEND-SECTION -->\n"
        '<section class="section-block" id="sec-node">\n'
        "      <h2>Node.js backend (this JD)</h2>\n"
        '<p style="color:var(--color-text-muted);font-size:var(--text-sm);margin:0 0 1rem">'
        "Spoken answers for a Node fullstack JD. Lead with IELTS (RN + Express + Cloud Run) "
        "and BaseVN PHP/MySQL. Nest and Mongo are a ramp — Express on IELTS is production.</p>\n"
        + "\n".join(articles)
        + "\n    </section>\n<!-- /NODE-BACKEND-SECTION -->\n"
    )
    rail = (
        "<!-- NODE-BACKEND-RAIL -->"
        f'<a class="parts-rail-link" href="#sec-node" data-part="sec-node">'
        f"<strong>Node.js backend</strong><span>{len(CARDS)} Q</span></a>"
        "<!-- /NODE-BACKEND-RAIL -->"
    )
    return "\n".join(toc), section, rail


def replace_block(text: str, start: str, end: str, new: str) -> str:
    if start in text and end in text:
        return re.sub(re.escape(start) + r".*?" + re.escape(end), new, text, count=1, flags=re.S)
    return text


def inject(text: str) -> str:
    toc, section, rail = toc_and_section()
    text = replace_block(text, "<!-- NODE-BACKEND-TOC -->", "<!-- /NODE-BACKEND-TOC -->", toc)
    text = replace_block(text, "<!-- NODE-BACKEND-SECTION -->", "<!-- /NODE-BACKEND-SECTION -->", section)
    text = replace_block(text, "<!-- NODE-BACKEND-RAIL -->", "<!-- /NODE-BACKEND-RAIL -->", rail)

    if "<!-- NODE-BACKEND-TOC -->" not in text:
        needle = '        <div class="side-toc-part" data-part="sec-php">'
        if needle not in text:
            raise SystemExit("cannot find PHP toc to insert Node in front of")
        text = text.replace(needle, toc + "\n" + needle, 1)

    if "<!-- NODE-BACKEND-SECTION -->" not in text:
        needle = '<section class="section-block" id="sec-php">'
        text = text.replace(needle, section + needle, 1)

    if "<!-- NODE-BACKEND-RAIL -->" not in text:
        needle = '<a class="parts-rail-link" href="#sec-php" data-part="sec-php">'
        text = text.replace(needle, rail + "\n        " + needle, 1)

    if 'href="#sec-node">Node.js</a>' not in text:
        text = text.replace(
            '<a href="#sec-php">PHP</a>',
            '<a href="#sec-node">Node.js</a>\n          <a href="#sec-php">PHP</a>',
            1,
        )

    text = text.replace(
        "Backend (PHP), frontend (React / TypeScript), fullstack integration, and system design.",
        "Backend (Node.js + PHP), frontend (React / TypeScript), fullstack integration, and system design.",
    )
    text = text.replace(
        'For a Node-first JD start at <a href="#sec-node">Node.js backend</a>. Soft-skill debug is on the Soft skills page. Be honest: PHP APIs are production-deep; Nest/Express/Mongo are a ramp, not a fake senior claim. Zustand: researched, not production.',
        'For a Node-first JD start at <a href="#sec-node">Node.js backend</a>. IELTS is the Express + RN proof; BaseVN is MySQL depth. Nest/Mongo are a ramp, not a fake senior claim. Zustand: researched, not production.',
    )
    text = text.replace(
        "Stack and design answers. Soft-skill debug process is on the Soft skills page. Be honest on Zustand: researched, not production.",
        'For a Node-first JD start at <a href="#sec-node">Node.js backend</a>. IELTS is the Express + RN proof; BaseVN is MySQL depth. Nest/Mongo are a ramp, not a fake senior claim. Zustand: researched, not production.',
    )
    return text


def patch_hub() -> None:
    p = ROOT / "index.html"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        "PHP backend, React/TS frontend, system design.",
        "Node.js + PHP backend, React/TS frontend, system design.",
    )
    t2 = t2.replace(
        "Akktis, IELTS AI Tutor, BaseVN walkthroughs and hard fixes.",
        "Akktis, IELTS AI Tutor (RN + Express), BaseVN walkthroughs and hard fixes.",
    )
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("patched index.html")


def patch_cv() -> None:
    """Tighten existing IELTS CV cards to match the real RN + Express work."""
    p = ROOT / "cv.html"
    t = p.read_text(encoding="utf-8")
    orig = t
    pairs = [
        (
            "On the side I ship client products like IELTS AI Tutor on Cloud Run.",
            "On the side I ship IELTS AI Tutor: React Native on both stores plus an Express API on Cloud Run.",
        ),
        (
            "Bên cạnh đó tôi ship sản phẩm khách như IELTS AI Tutor trên Cloud Run.",
            "Bên cạnh đó tôi ship IELTS AI Tutor: React Native trên hai store và API Express trên Cloud Run.",
        ),
        (
            "It's a mobile IELTS learning app for iOS and Android, plus a teacher assignment portal. I built the mobile side, AI-supported practice features, and kept backend services running on Google Cloud Run. It's live on Google Play and the App Store.".replace("It's", "It\u2019s"),
            "It's a mobile IELTS learning app for iOS and Android, plus a teacher assignment portal. I built the Expo React Native/TypeScript client \u2014 skills practice, study plan, IAP, ads, Google/Apple login \u2014 and the Express backend on Cloud Run: auth, practice content, AI tutor, TTS/STT, progress storage, purchase webhooks. It's live on Google Play and the App Store.".replace("It's", "It\u2019s"),
        ),
        (
            "Đây là app học IELTS trên iOS/Android, kèm portal giao bài cho giáo viên. Tôi làm phía mobile, tính năng AI hỗ trợ luyện tập, và giữ backend trên Google Cloud Run. App đã lên Google Play và App Store.",
            "Đây là app học IELTS trên iOS/Android, kèm portal giao bài cho giáo viên. Tôi làm client Expo React Native/TypeScript — luyện skill, study plan, IAP, ads, login Google/Apple — và backend Express trên Cloud Run: auth, nội dung luyện, AI tutor, TTS/STT, lưu tiến độ, webhook mua hàng. App đã lên Google Play và App Store.",
        ),
        (
            "Built RN/TS app, portal workflows, AI features, Cloud Run backend.",
            "Built RN/TS app and Express APIs; portal workflows; Cloud Run ops.",
        ),
        (
            "End-to-end ownership: mobile, portal link, cloud backend.",
            "End-to-end: React Native client + Express API + Cloud Run.",
        ),
        (
            "Cloud Run fit a containerized backend without managing nodes. I deployed and maintained those services — releases, logs, and day-to-day cloud operations so the mobile app and portal stayed connected.",
            "Cloud Run fit a containerized Express API without managing nodes. I deploy and maintain that Node service — releases, logs, revisions — so the React Native app and teacher portal stay connected. Same Cloud Run muscle I use at Akktis, applied to this product.",
        ),
        (
            "Cloud Run hợp backend container mà không phải quản lý node. Tôi deploy và maintain các service đó — release, log, và vận hành cloud hằng ngày để app và portal vẫn kết nối được.",
            "Cloud Run hợp API Express đóng container mà không phải quản lý node. Tôi deploy và maintain service Node đó — release, log, revision — để app React Native và portal giáo viên còn kết nối. Cùng cơ Cloud Run ở Akktis, áp vào sản phẩm này.",
        ),
        (
            "I integrated chat completion, text-to-speech, and speech-to-text into the learning workflows — so students can practice and get AI-supported feedback inside the real app, not as a separate demo.",
            "The phone never holds the OpenAI key. Chat completion goes through Express /api/agent with skill-specific prompts. TTS is /api/tts, STT is /api/transcribe. Writing scores use four IELTS band prompts. I wrap OpenAI with Langfuse so a weird answer is a trace. I integrate models into learning workflows — I don't train them.",
        ),
        (
            "Tôi tích hợp chat completion, text-to-speech và speech-to-text vào workflow học — học viên luyện và nhận hỗ trợ AI ngay trong app thật, không phải demo tách rời.",
            "Điện thoại không giữ key OpenAI. Chat đi Express /api/agent với prompt theo skill. TTS là /api/tts, STT là /api/transcribe. Chấm writing dùng bốn prompt band IELTS. Tôi bọc OpenAI bằng Langfuse nên câu lạ là trace. Tôi gắn model vào workflow học — không train model.",
        ),
        (
            "Teachers use the portal for assignments and workflows; students practice on mobile. I supported the communication between app and portal and the cloud operations behind that link, so both sides stay in sync for learning tasks.",
            "Teachers use the portal for classes, assignments, and submissions; students practice on mobile. Both hit the same Express API. Assignment data lives in Firestore. I keep the contract on the server so we don't duplicate assignment rules in two clients.",
        ),
        (
            "Giáo viên dùng portal để giao bài và workflow; học viên luyện trên mobile. Tôi hỗ trợ giao tiếp app–portal và phần cloud phía sau, để hai bên đồng bộ cho việc học.",
            "Giáo viên dùng portal cho class, assignment, submission; học viên luyện trên mobile. Cả hai gọi cùng API Express. Data assignment nằm trên Firestore. Tôi giữ contract trên server để không nhân đôi rule assignment ở hai client.",
        ),
    ]
    for old, new in pairs:
        t = t.replace(old, new)
    if t != orig:
        p.write_text(t, encoding="utf-8")
        print(f"patched cv.html bytes={p.stat().st_size}")
    else:
        print("cv.html already patched or strings not found")


def main() -> None:
    raw = ENG.read_text(encoding="utf-8")
    out = inject(raw)
    ENG.write_text(out, encoding="utf-8")
    print(f"wrote {ENG} bytes={ENG.stat().st_size} node_cards={len(CARDS)}")
    patch_hub()
    patch_cv()
    if 'id="sec-node"' not in out:
        raise SystemExit("inject failed: sec-node missing")
    if 'id="n1"' not in out or 'id="n30"' not in out:
        raise SystemExit("inject failed: node cards missing")


if __name__ == "__main__":
    main()
