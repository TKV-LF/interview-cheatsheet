# Card data: fit / scenarios / closing from real experience. Synthetic study content only.
# Intended importer (future regenerator): from cards_interview import CARDS
# Shape: {sec, kind:"interview", title, sub, q_en, a_en, q_vi, a_vi, star?} — no date fields.
# Spoken first-person EN/VI. Spine: Cloud Build + Cloud Run + Linux VM + mobile CI.


def I(sec, title, sub, q_en, a_en, q_vi, a_vi, star=""):
    return {"sec": sec, "kind": "interview", "title": title, "sub": sub,
            "q_en": q_en, "a_en": a_en, "q_vi": q_vi, "a_vi": a_vi, "star": star}


CARDS = [
    # ── sec-fit ───────────────────────────────────────────────────────────────
    I("sec-fit", "Tell me about yourself (DevOps)", "60–90s spoken intro",
      "Tell me about yourself.",
      "I'm a full-stack engineer who also owns delivery and ops. At Akktis I work across Linux servers over SSH — Ubuntu and Debian — CI/CD for mobile and web across environments, and Google Cloud: Cloud Run, Cloud SQL, and Storage. I also operate LiteSpeed and Apache for PHP and CMS apps, and I care about docs and basic hardening so systems are safer to hand off. Independently I shipped IELTS AI Tutor — a React Native and TypeScript app on iOS and Android with a Cloud Run backend, live on Google Play and the App Store. I'm looking for a DevOps-focused role where I can deepen that spine: pipelines, cloud deploys, and reliable Linux operations.",
      "Hãy giới thiệu về bản thân.",
      "Tôi là full-stack kiêm delivery và ops. Ở Akktis tôi làm Linux qua SSH — Ubuntu và Debian — CI/CD cho mobile và web multi-env, và Google Cloud: Cloud Run, Cloud SQL và Storage. Tôi cũng operate LiteSpeed và Apache cho app PHP/CMS, và quan tâm docs cùng harden cơ bản để handoff an toàn hơn. Bên cạnh đó tôi ship IELTS AI Tutor — app React Native/TypeScript trên iOS và Android với backend Cloud Run, đã lên Google Play và App Store. Tôi muốn role nghiêng DevOps để đào sâu spine đó: pipeline, deploy cloud và Linux ops ổn định."),

    I("sec-fit", "Strengths for a DevOps role", "Concrete, not buzzwords",
      "What are your strengths?",
      "First, I bridge app and ops — I can read application failures and infra failures in the same incident. Second, I have hands-on delivery paths I've actually run: mobile CI toward store builds, Cloud Build into Cloud Run, and classic VM web servers with Nginx/Apache/LiteSpeed. Third, I debug with evidence — pipeline logs, Cloud Run revisions, SSH logs and disk — then mitigate first and document so the gap doesn't repeat. I'm honest about depth: Cloud Run and Linux VMs are my spine; I don't pretend deep Kubernetes HA if that's not what I've operated day to day.",
      "Điểm mạnh của bạn là gì?",
      "Một, tôi bridge app và ops — đọc được lỗi application và lỗi infra trong cùng incident. Hai, tôi có delivery path thật: CI mobile tới store build, Cloud Build vào Cloud Run, và classic VM web server với Nginx/Apache/LiteSpeed. Ba, tôi debug bằng evidence — pipeline log, revision Cloud Run, SSH log và disk — mitigate trước rồi document để không lặp. Tôi trung thực về độ sâu: Cloud Run và Linux VM là spine; tôi không claim sâu Kubernetes HA nếu đó không phải việc hằng ngày."),

    I("sec-fit", "Tool walkthrough", "Stack I can defend",
      "Walk me through your DevOps tool stack.",
      "Source control is Git. CI is Cloud Build or a generic CI runner on push and tags — build, test when we have them, package artifacts. For backends I Dockerize, push to Artifact Registry, and deploy Cloud Run with env and secrets, often wired to Cloud SQL and Cloud Storage. For mobile, React Native builds produce Android AAB/APK and iOS IPA concepts with signing material kept in secrets, then artifacts go to storage or store tracks. For classic web I SSH into Ubuntu/Debian, manage LiteSpeed or Apache or Nginx, firewall and TLS, and keep short runbooks. Day to day observability is Cloud Logging on Run and system/web logs on VMs.",
      "Hãy mô tả stack DevOps của bạn.",
      "Source control là Git. CI là Cloud Build hoặc CI runner generic theo push và tag — build, test khi có, package artifact. Backend tôi Dockerize, push Artifact Registry, deploy Cloud Run với env và secret, thường wire Cloud SQL và Cloud Storage. Mobile, build React Native ra AAB/APK Android và khái niệm IPA iOS, signing nằm trong secret, artifact lên storage hoặc store track. Classic web tôi SSH Ubuntu/Debian, quản LiteSpeed hoặc Apache hoặc Nginx, firewall và TLS, giữ runbook ngắn. Observability hằng ngày là Cloud Logging trên Run và system/web log trên VM."),

    I("sec-fit", "Why a DevOps role?", "Generic company — honest motivation",
      "Why do you want this DevOps role?",
      "Because I already enjoy the ownership from commit to a healthy environment, and I want that to be the center of my work — not only a side of full-stack. Your role is about reliable delivery: CI/CD, cloud or Linux operations, and helping developers ship safely. That matches what I do at Akktis and on IELTS AI Tutor, and I want to go deeper on pipeline quality, environment promotion, and operational hygiene in a team that takes infra seriously.",
      "Tại sao bạn muốn role DevOps này?",
      "Vì tôi đã thích ownership từ commit đến env healthy, và muốn đó là trọng tâm công việc — không chỉ phần phụ của full-stack. Role của các bạn là delivery tin cậy: CI/CD, cloud hoặc Linux ops, và giúp developer ship an toàn. Điều đó khớp việc tôi làm ở Akktis và IELTS AI Tutor, và tôi muốn đào sâu chất lượng pipeline, promote env và ops hygiene trong team coi trọng infra."),

    I("sec-fit", "Akktis day-to-day", "What ops looks like",
      "What does a typical ops-heavy day look like for you?",
      "It depends on the project, but usually I'm either unblocking a release or keeping an environment healthy. That means checking CI status for web or mobile, SSH into a Linux box to read logs or restart a service, verifying a Cloud Run revision after deploy, or fixing env and connectivity to Cloud SQL or Storage. I also touch LiteSpeed or Apache when a PHP or CMS site misbehaves, and I update docs when I find tribal knowledge that would hurt the next person.",
      "Một ngày nghiêng ops của bạn trông thế nào?",
      "Tùy project, nhưng thường tôi hoặc unblock release, hoặc giữ env healthy. Tức là check status CI web hoặc mobile, SSH vào Linux đọc log hoặc restart service, verify revision Cloud Run sau deploy, hoặc fix env và connectivity tới Cloud SQL hay Storage. Tôi cũng đụng LiteSpeed hoặc Apache khi site PHP/CMS lỗi, và update docs khi gặp tribal knowledge — dễ hại người sau."),

    I("sec-fit", "Weakness (honest)", "Time-box vs polish",
      "What's a weakness relevant to this job?",
      "I can over-invest in polishing a pipeline or runbook when a smaller safe mitigation would unblock the team sooner. I've learned to time-box: ship the safe fix or rollback first, communicate status, then harden the checklist so we don't pay twice.",
      "Một điểm yếu liên quan job này?",
      "Tôi đôi khi invest quá nhiều để polish pipeline hoặc runbook trong khi một mitigation nhỏ an toàn đã unblock được team. Tôi đã học time-box: ship fix an toàn hoặc rollback trước, báo status, rồi harden checklist để không trả giá hai lần."),

    # ── sec-scenario ──────────────────────────────────────────────────────────
    I("sec-scenario", "Broken mobile pipeline", "Android/iOS CI red",
      "The mobile CI pipeline that was green yesterday is failing today. What do you do?",
      "I start from what changed — last commits, dependency lockfile, CI image or Xcode/SDK version, and whether signing secrets or provisioning profiles expired. I open the first failing stage log, not the last noise. If it's signing, I validate keystore or profile access before re-running a long compile. If it's Gradle or native modules, I try to reproduce with the same Node and JDK locally. I unblock with a revert or pin if a release is blocked, tell the team status, then fix forward and note it in the runbook.",
      "Pipeline mobile hôm qua green hôm nay đỏ. Bạn làm gì?",
      "Tôi bắt đầu từ thứ đã đổi — commit, lockfile dependency, CI image hoặc version Xcode/SDK, và signing secret hay provisioning profile có hết hạn không. Tôi mở log stage fail đầu tiên, không đọc noise cuối. Nếu là signing, tôi validate keystore hoặc profile trước khi re-run compile dài. Nếu là Gradle hoặc native module, tôi cố reproduce cùng Node và JDK local. Tôi unblock bằng revert hoặc pin nếu release bị block, báo team, rồi fix forward và ghi runbook.",
      "S: Mobile CI failed before store upload\nT: Unblock a release build same day\nA: Compared last green, fixed signing/deps, re-ran pipeline\nR: Green artifact; checklist updated for secret expiry"),

    I("sec-scenario", "Bad Cloud Run revision", "Rollback under pressure",
      "You deployed to Cloud Run and error rates spiked. How do you respond?",
      "I treat it as a revision problem first. I check Cloud Logging filtered to the new revision, confirm it's the deploy that correlates with the spike, then shift traffic back to the last healthy revision while I investigate. Common causes for me are missing env or secret on the new revision, Cloud SQL connectivity, or an app bug that only shows with prod config. After users are stable I fix forward, redeploy, and optionally canary before 100%.",
      "Bạn deploy Cloud Run rồi error rate tăng. Xử lý thế nào?",
      "Tôi coi đây là vấn đề revision trước. Check Cloud Logging filter revision mới, confirm spike khớp deploy, rồi chuyển traffic về revision healthy trước trong khi investigate. Nguyên nhân hay gặp với tôi: thiếu env hoặc secret trên revision mới, Cloud SQL connectivity, hoặc bug app chỉ lộ với config prod. Sau khi user ổn tôi fix forward, deploy lại, và có thể canary trước khi 100%.",
      "S: New Cloud Run revision elevated 5xx\nT: Restore availability quickly\nA: Traffic to previous revision; diff env/logs; fix and redeploy\nR: Service healthy; noted canary for riskier changes"),

    I("sec-scenario", "VM disk full", "Classic Linux fire",
      "A production website on a Linux VM is down or can't write files. Disk looks full. What do you do?",
      "I SSH in, confirm with df -h and df -i, and find what's consuming space — often logs, old backups, or uploads. I free space safely: rotate or truncate known log files, move old backups off the box, never delete database directories I don't understand. I verify the site and PHP or web server logs recover. Then I fix root cause — logrotate, retention, or a larger disk — and document it so the next full-disk isn't a surprise.",
      "Website trên VM Linux lỗi hoặc không ghi được file. Disk đầy. Bạn làm gì?",
      "Tôi SSH vào, confirm với df -h và df -i, tìm thứ chiếm chỗ — thường log, backup cũ hoặc upload. Free space an toàn: rotate hoặc truncate log đã biết, chuyển backup cũ khỏi máy, không xóa directory database không hiểu. Verify site và log PHP/web server hồi. Rồi fix root cause — logrotate, retention, hoặc tăng disk — và document để lần full disk sau không bất ngờ.",
      "S: CMS site failing writes on Ubuntu VM\nT: Restore writes without data loss\nA: df/du, cleared logs/backups safely, verified Nginx/Apache\nR: Site writable; retention added"),

    I("sec-scenario", "Cloud SQL unreachable from Cloud Run", "Connectivity isolation",
      "Cloud Run can't reach Cloud SQL after a deploy. How do you debug?",
      "I isolate layers: did the new revision lose the Cloud SQL connection annotation or the secret for the DB password? Is the service account still allowed? Is the app using the right connection name or socket path? I compare the last healthy revision's config to the new one, check Cloud Logging for connection refused or auth errors, and verify the instance is up. I don't open the database to the public internet as a shortcut — I fix the connector, IAM, or secret wiring.",
      "Cloud Run không tới được Cloud SQL sau deploy. Bạn debug thế nào?",
      "Tôi isolate layer: revision mới có mất annotation kết nối Cloud SQL hoặc secret DB password không? Service account còn quyền không? App có đúng connection name hoặc socket path không? Tôi so config revision healthy với bản mới, xem Cloud Logging lỗi connection refused hoặc auth, và confirm instance còn sống. Tôi không mở database ra public internet để xong việc — tôi fix connector, IAM hoặc secret wiring.",
      "S: API 500s; logs show DB connection failure\nT: Restore DB connectivity without exposing SQL publicly\nA: Diff Run SQL settings/secrets/IAM; fix wiring; verify /health\nR: Connections restored; checklist for SQL on deploy"),

    I("sec-scenario", "Release under time pressure", "Safe speed",
      "Stakeholders want a release today but CI is flaky and staging isn't fully verified. What do you do?",
      "I separate must-ship from nice-to-have. I won't skip signing checks or push an unsigned mobile build, and I won't deploy a Cloud Run image I can't roll back. I will time-box: identify the smallest safe artifact that already passed a meaningful check, smoke the critical path on staging, deploy with a clear rollback owner, and communicate risk honestly. If the risk is too high, I say so with options — delay, reduced scope, or hotfix-only — instead of silent hope.",
      "Stakeholder muốn release hôm nay nhưng CI flaky và staging chưa verify đủ. Bạn làm gì?",
      "Tôi tách must-ship khỏi nice-to-have. Tôi không bỏ signing check hay đẩy bản mobile chưa sign, và không deploy image Cloud Run mà không rollback được. Tôi time-box: chọn artifact nhỏ nhất an toàn đã qua check có nghĩa, smoke critical path trên staging, deploy với người own rollback rõ, và nói risk thẳng. Nếu risk quá cao, tôi nói kèm option — delay, giảm scope, hoặc chỉ hotfix — thay vì hy vọng thầm.",
      "S: Business wants same-day release; CI unstable\nT: Protect users while enabling minimum ship\nA: Scoped release, smoke, rollback plan, honest status\nR: Shipped reduced scope or delayed with clear rationale"),

    I("sec-scenario", "Staging OK, prod fails", "Multi-env delta",
      "Staging looks fine but production fails right after promote. What's your approach?",
      "I assume config drift until proven otherwise — env vars, secrets, web server vhost differences, API URLs in the mobile build, or Cloud SQL instance differences. I compare what actually differs between environments, not only the git sha. I've seen this a lot with multi-env CI/CD: missing prod secret, different LiteSpeed/Apache setting, or an app pointing at the wrong backend. Fix the delta, redeploy, and update the promotion checklist.",
      "Staging ổn nhưng production fail ngay sau promote. Bạn tiếp cận thế nào?",
      "Tôi giả định config drift cho đến khi chứng minh ngược — env, secret, khác vhost web server, API URL trong bản mobile, hoặc khác instance Cloud SQL. Tôi so thứ thực sự khác giữa env, không chỉ git sha. Tôi hay gặp với CI/CD multi-env: thiếu secret prod, setting LiteSpeed/Apache khác, hoặc app trỏ nhầm backend. Fix delta, deploy lại, update checklist promote.",
      "S: Promote to prod failed after green staging\nT: Restore prod; prevent repeat\nA: Diff env/secrets/web config; fix; checklist\nR: Prod healthy; promotion gap documented"),

    # ── sec-close ─────────────────────────────────────────────────────────────
    I("sec-close", "Questions to ask them", "Show judgment",
      "Do you have any questions for us?",
      "I'd ask how you promote from staging to production today — tags, approvals, or automatic. I'd ask what observability looks like for the services I'd own on week one — logs, alerts, on-call expectations. And I'd ask where the team feels the most pain right now: flaky CI, cloud cost, Linux snowflake servers, or mobile release friction — so I know where I can help first.",
      "Bạn có câu hỏi gì cho chúng tôi không?",
      "Tôi sẽ hỏi hiện team promote staging lên production thế nào — tag, approval, hay automatic. Tôi hỏi observability cho service tôi sẽ own tuần đầu trông ra sao — log, alert, kỳ vọng on-call. Và tôi hỏi chỗ team đang đau nhất: CI flaky, cloud cost, Linux snowflake server, hay friction release mobile — để biết tôi giúp gì trước."),

    I("sec-close", "60s closing pitch", "Honest stack, clear intent",
      "Anything else you'd like us to remember?",
      "Just briefly: I bring hands-on delivery on GCP Cloud Run, Cloud SQL, and Storage, Linux VM operations with SSH, LiteSpeed and Apache, and CI/CD for web and mobile — including a React Native app published on both stores with a Cloud Run backend. I'm intentionally going deeper into DevOps — pipeline quality, environment promotion, and reliable operations — and I'm honest about where I'm strong versus where I'd ramp. I'm ready to contribute from day one on deploys, troubleshooting, and making releases less fragile.",
      "Bạn muốn chúng tôi nhớ thêm điều gì?",
      "Ngắn gọn: tôi mang delivery thực tế trên GCP Cloud Run, Cloud SQL và Storage, Linux VM ops qua SSH, LiteSpeed và Apache, và CI/CD cho web lẫn mobile — gồm app React Native đã publish cả hai store với backend Cloud Run. Tôi chủ đích đào sâu DevOps — chất lượng pipeline, promote env và ops tin cậy — và nói thẳng chỗ mạnh với chỗ sẽ ramp. Tôi sẵn sàng contribute từ sớm ở deploy, troubleshoot và làm release less fragile."),

    I("sec-close", "Ramp-up honesty", "If they probe a JD tool you don't live in",
      "We use Jenkins and Kubernetes heavily. How would you ramp up?",
      "I'd be honest: my daily spine is Cloud Build, Cloud Run, Linux VMs, and mobile CI — not operating Kubernetes HA clusters or a large Jenkins estate as my primary job. The underlying skills transfer — pipeline stages, artifacts, secrets, rollbacks, logs. I'd ramp by pairing on your existing pipelines, reading your runbooks, and delivering small owned changes first, while mapping your Jenkins or Kubernetes stages to patterns I already know.",
      "Chúng tôi dùng nhiều Jenkins và Kubernetes. Bạn ramp-up thế nào?",
      "Tôi nói thẳng: spine hằng ngày của tôi là Cloud Build, Cloud Run, Linux VM và CI mobile — không phải operate cluster Kubernetes HA hay hệ Jenkins lớn như việc chính. Skill nền transfer được — stage pipeline, artifact, secret, rollback, log. Tôi ramp bằng pair trên pipeline sẵn có, đọc runbook, và nhận change nhỏ có ownership trước, đồng thời map stage Jenkins hoặc Kubernetes sang pattern tôi đã biết."),
]
