# Card data: slim general DevOps fundamentals. Synthetic study content only.
# Intended importer (future regenerator): from cards_fundamentals import CARDS
# Shape: {sec, kind, title, sub, c_en, m_en, c_vi, m_vi, crib?, note?} — no date fields.
# Keep SHORT. General fundamentals only — no vendor JD jargon, no MCQ.


def C(sec, title, sub, c_en, m_en, c_vi, m_vi, crib="", note=""):
    return {"sec": sec, "kind": "concept", "title": title, "sub": sub,
            "c_en": c_en, "m_en": m_en, "c_vi": c_vi, "m_vi": m_vi,
            "crib": crib, "note": note}


CARDS = [
    # ── sec-devops ────────────────────────────────────────────────────────────
    C("sec-devops", "What is DevOps?", "Culture + automation + ownership",
      "DevOps shortens the path from commit to reliable production by combining shared ownership, automation, measurement, and fast feedback between people who build and people who run systems.",
      "Tools enable DevOps; they don't replace clear ownership of build, deploy, monitor, and recover.",
      "DevOps rút ngắn path từ commit đến production ổn định bằng ownership chung, automation, đo lường và feedback nhanh giữa người build và người operate.",
      "Tool hỗ trợ DevOps; không thay ownership rõ về build, deploy, monitor và recover.",
      "DevOps ≠ installing one CI product."),

    C("sec-devops", "CI vs CD", "Precise meanings",
      "CI (Continuous Integration): automatically build and test every change so the main line stays healthy. CD usually means Continuous Delivery (always releasable with a human gate) or Continuous Deployment (auto to production).",
      "Say which CD meaning you use. CI without automated tests is mostly packaging.",
      "CI: tự động build/test mỗi change để main line healthy. CD thường là Continuous Delivery (luôn sẵn sàng release, có approval gate) hoặc Continuous Deployment (auto lên production).",
      "Nói rõ bạn đang dùng nghĩa CD nào. CI không có test tự động thì chủ yếu là package.",
      "Saying 'we do CD' without explaining the prod gate is vague."),

    C("sec-devops", "Pipeline stages mental model", "Commit to verify",
      "A typical pipeline: checkout → install/build → test → package artifact (image/AAB) → deploy to an environment → notify. Secrets stay outside Git; prod often needs an extra approval or tag.",
      "Be able to point where your real work sits: Cloud Build → Artifact Registry → Cloud Run, or CI → mobile store track, or rsync/git pull on a VM.",
      "Pipeline điển hình: checkout → install/build → test → package artifact (image/AAB) → deploy env → notify. Secret ngoài Git; prod thường cần approval hoặc tag.",
      "Chỉ được chỗ công việc thật của bạn: Cloud Build → Artifact Registry → Cloud Run, hoặc CI → track store mobile, hoặc rsync/git pull trên VM.",
      "Memorizing stage names without a real failure story is weak."),

    C("sec-devops", "Why multi-environment matters", "dev / staging / prod",
      "Separate environments reduce blast radius: try changes in staging with staging data/secrets before production. Promotion should be deliberate — same artifact when possible, different config.",
      "Staging green with wrong API URL still breaks prod. Always name the config delta.",
      "Tách env giúp giảm blast radius: thử ở staging với data/secret staging trước production. Promote có chủ đích — cùng artifact khi được, khác config.",
      "Staging green nhưng sai API URL vẫn phá prod. Luôn nêu delta config.",
      "One shared 'prod-like' box for everything is not multi-env."),

    # ── sec-linux ─────────────────────────────────────────────────────────────
    C("sec-linux", "SSH day-to-day", "How you actually manage hosts",
      "SSH into Ubuntu/Debian, check service status, logs, disk/memory, apply the safest fix, verify. Prefer key-based auth and a sudo user over root password login.",
      "Structured loop: symptom → resources → logs → recent changes → fix → verify.",
      "SSH vào Ubuntu/Debian, xem status service, log, disk/memory, apply fix an toàn nhất, verify. Ưu tiên SSH key và sudo user hơn login root bằng password.",
      "Loop có cấu trúc: symptom → resource → log → change gần đây → fix → verify.",
      "Random reboot without checking logs hides root cause.",
      "ssh user@host\nsystemctl status nginx\njournalctl -u nginx -n 50\ndf -h"),

    C("sec-linux", "Processes, services, permissions", "Just enough OS",
      "Know how to list processes, restart systemd services, and read rwx permissions. Prefer fixing ownership/group over chmod 777. Long-running jobs belong under systemd, not forgotten nohup.",
      "id / ls -l / systemctl / journalctl are interview-safe everyday tools.",
      "Biết list process, restart service systemd, đọc quyền rwx. Ưu tiên fix ownership/group hơn chmod 777. Job dài nên nằm dưới systemd, không nohup quên.",
      "id / ls -l / systemctl / journalctl là tool hằng ngày an toàn khi interview.",
      "chmod 777 to unblock uploads is a security smell.",
      "ps aux | head\nsudo systemctl restart php8.2-fpm\nls -l /var/www"),

    C("sec-linux", "Disk and log hygiene", "Classic outage cause",
      "Full disks break writes, CMS uploads, and sometimes SSH usability in subtle ways. Watch df -h, rotate logs, and keep backups off the app volume when possible.",
      "Never delete unknown database directories to free space.",
      "Disk đầy làm hỏng ghi file, upload CMS, đôi khi SSH cũng lạ. Theo dõi df -h, rotate log, giữ backup khỏi volume app khi được.",
      "Không xóa directory database không rõ để free space.",
      "df green on size but inodes full (df -i) still breaks creates.",
      "df -h; df -i\nsudo du -xh /var/log | sort -h | tail"),

    C("sec-linux", "Package basics on Debian/Ubuntu", "apt awareness",
      "apt update refreshes indexes; apt install adds packages; prefer understanding what a package starts (nginx, php-fpm) before upgrading production blindly.",
      "Patch on a schedule; know how to roll back a bad package upgrade if the team has a pattern.",
      "apt update làm mới index; apt install thêm package; hiểu package start gì (nginx, php-fpm) trước khi upgrade prod blindly.",
      "Patch theo schedule; biết rollback upgrade package xấu nếu team có pattern.",
      "apt upgrade on prod Friday evening without a window is a risk.",
      "sudo apt update\nsudo apt install -y nginx"),

    # ── sec-git ───────────────────────────────────────────────────────────────
    C("sec-git", "Branching for delivery", "What CI watches",
      "Feature branches for work; protected main for integration; tags for release candidates. CI triggers usually bind to branch or tag patterns.",
      "Say how your team promotes: merge to main → staging deploy; tag → prod/mobile release.",
      "Feature branch cho work đang làm; main được protect để integrate; tag cho release candidate. CI thường gắn pattern branch hoặc tag.",
      "Nói team promote thế nào: merge main → deploy staging; tag → prod/mobile release.",
      "Force-push to shared main is an interview red flag."),

    C("sec-git", "PR collaboration basics", "Review before build cost",
      "Pull requests catch bad config and secret leaks before expensive mobile/cloud builds. Small diffs review faster than mega-PRs.",
      "CI on PR should be cheaper than full store/prod deploy — lint/test first.",
      "Pull request bắt config xấu và secret leak trước khi burn native/cloud build. Diff nhỏ review nhanh hơn mega-PR.",
      "CI trên PR nên rẻ hơn full deploy store/prod — lint/test trước.",
      "Merging with red CI 'because it's flaky' without checking is a habit to break."),

    C("sec-git", "What changed? incident habit", "Git as forensics",
      "When production breaks after a release, compare the last green commit to HEAD: app code, Dockerfile, cloudbuild.yaml, env templates.",
      "git log / git diff / revert or rollback image are first-class ops tools.",
      "Khi production break sau release, so last green commit với HEAD: code app, Dockerfile, cloudbuild.yaml, template env.",
      "git log / git diff / revert hoặc rollback image là tool ops hạng nhất.",
      "Blaming Git instead of reading the diff wastes time.",
      "git log --oneline -10\ngit diff HEAD~1"),

    C("sec-git", "Secrets never in Git", "Hard rule",
      "Keystores, .env with passwords, cloud keys, and private keys must not be committed. Use Secret Manager / CI secrets and .gitignore.",
      "If a secret is committed, rotate it — removing from history alone is not enough if it was pushed.",
      "Keystore, .env có password, cloud key và private key không được commit. Dùng Secret Manager / secret CI và .gitignore.",
      "Nếu secret đã commit, phải rotate — chỉ xóa khỏi history chưa đủ nếu đã push.",
      "git-crypt stories without rotation still leave leaked credentials usable."),

    # ── sec-docker ────────────────────────────────────────────────────────────
    C("sec-docker", "Why containers for Cloud Run", "Same artifact everywhere",
      "A container packages the app and its runtime so staging and Cloud Run run the same bits. You ship an image tag/digest, not 'it works on my laptop'.",
      "Dockerfile + listen on $PORT is the Cloud Run baseline.",
      "Container package app và runtime để staging và Cloud Run chạy cùng bits. Bạn ship image tag/digest, không phải 'chạy được trên laptop'.",
      "Dockerfile + listen $PORT là baseline Cloud Run.",
      "Treating a container like a full VM (SSH in to patch live) fights the model."),

    C("sec-docker", "Image layers & .dockerignore", "Build speed and size",
      "Order Dockerfile so dependency layers cache. Exclude .git and local node_modules via .dockerignore. Smaller images pull and start faster.",
      "Don't COPY secrets into any layer.",
      "Sắp xếp Dockerfile để layer deps được cache. Exclude .git và node_modules local bằng .dockerignore. Image nhỏ pull và start nhanh hơn.",
      "Không COPY secret vào bất kỳ layer nào.",
      "COPY . early invalidates cache on every code tweak.",
      "docker build -t api:local .\ndocker images"),

    C("sec-docker", "Run locally then deploy", "Parity check",
      "Run the image locally with the same PORT and critical env vars before trusting a Cloud Run deploy. Diff local success vs Cloud Run failure → usually env, secrets, or Cloud SQL connectivity.",
      "Local green does not prove IAM/VPC/SQL wiring.",
      "Chạy image local với cùng PORT và env quan trọng trước khi tin deploy Cloud Run. Local OK nhưng Cloud Run fail → thường env, secret, hoặc Cloud SQL connectivity.",
      "Local green không chứng minh IAM/VPC/SQL đã đúng.",
      "docker run --rm -p 8080:8080 -e PORT=8080 api:local"),

    C("sec-docker", "Tagging discipline", "Rollback needs names",
      "Tag images with git sha or build id in Artifact Registry. Prefer deploying immutable tags/digests over floating :latest in production.",
      "Rollback = point Cloud Run at the previous known-good tag/digest.",
      "Tag image bằng git sha hoặc build id trên Artifact Registry. Ưu tiên tag/digest immutable hơn :latest trên production.",
      "Rollback = trỏ Cloud Run về tag/digest known-good trước đó.",
      ":latest with no record of what sha it was is fuzzy ops."),

    # ── sec-gcp ───────────────────────────────────────────────────────────────
    C("sec-gcp", "GCP mental model", "Pick the right compute",
      "Cloud Run: managed containers, scale with requests. Compute Engine VM: full OS control for classic web stacks (LiteSpeed/Apache/Nginx). Cloud SQL: managed DB. Cloud Storage: files/artifacts. Cloud Build: CI that builds and can deploy.",
      "I choose Run when the app is containerized and request-driven; VM when I need long-lived custom web server control.",
      "Cloud Run: container managed, scale theo request. Compute Engine VM: full OS control cho classic web stack (LiteSpeed/Apache/Nginx). Cloud SQL: managed DB. Cloud Storage: file/artifact. Cloud Build: CI build và có thể deploy.",
      "Tôi chọn Run khi app đã container và theo request; VM khi cần control web server lâu dài, tùy biến.",
      "Don't claim GKE HA depth if your spine is Run + VM."),

    C("sec-gcp", "IAM & service accounts", "Who can do what",
      "Human users and Cloud Build/Cloud Run service accounts need least privilege: push images, deploy a service, read specific secrets — not project Owner for daily CI.",
      "Incidents often start with 'who has keys' and 'which SA deployed this revision'.",
      "Human user và service account Cloud Build/Cloud Run cần least privilege: push image, deploy service, đọc secret cụ thể — không cần Owner project cho CI hằng ngày.",
      "Incident thường bắt đầu từ 'ai giữ key' và 'SA nào deploy revision này'.",
      "Personal user ADC in CI is an audit smell."),

    C("sec-gcp", "Cloud Logging & revisions", "Observe what you ship",
      "Cloud Run revisions + Cloud Logging are the primary debug surfaces. VMs use journalctl and web server error logs. Always bind an error to a revision or deploy time.",
      "Rollback traffic first; dig root cause second.",
      "Revision Cloud Run + Cloud Logging là mặt debug chính. VM dùng journalctl và error log web server. Luôn gắn error với revision hoặc thời điểm deploy.",
      "Rollback traffic trước; dig root cause sau.",
      "Restart without identifying the revision loses the plot."),

    C("sec-gcp", "Storage vs SQL vs secrets", "Put data in the right place",
      "Cloud Storage for objects/artifacts; Cloud SQL for relational data; Secret Manager for credentials. Don't store passwords in Storage objects marked public.",
      "App config: non-secret env OK; credentials → secrets.",
      "Cloud Storage cho object/artifact; Cloud SQL cho relational data; Secret Manager cho credential. Không để password trong object Storage public.",
      "Config app: non-secret env OK; credential → secret.",
      "Public bucket 'for testing' that still has prod dumps is a breach waiting."),

    # ── sec-web ───────────────────────────────────────────────────────────────
    C("sec-web", "Nginx/Apache role", "Reverse proxy & static",
      "Web servers terminate HTTP(S), serve static files, and reverse-proxy or hand off to PHP-FPM/app processes. Misconfigured vhosts show up as wrong site, 502, or PHP download instead of execute.",
      "Always nginx -t / configtest before reload.",
      "Web server terminate HTTP(S), serve static, reverse-proxy hoặc hand off PHP-FPM/app. Vhost sai → nhầm site, 502, hoặc download file PHP thay vì execute.",
      "Luôn nginx -t / configtest trước reload.",
      "Blaming only the app when Host/root is wrong wastes time."),

    C("sec-web", "Virtual host basics", "server_name + root",
      "Each site needs server_name (or ServerName), document root, and log paths. Laravel-style apps usually point root at public/. TLS sits on the same vhost after Certbot.",
      "DNS A record must match the VM before public HTTPS works.",
      "Mỗi site cần server_name (hoặc ServerName), document root và log path. App kiểu Laravel thường trỏ root vào public/. TLS gắn cùng vhost sau Certbot.",
      "DNS A phải khớp VM trước khi HTTPS public chạy.",
      "Two vhosts with the same server_name fight unpredictably."),

    C("sec-web", "LiteSpeed awareness", "Same concepts, different panel",
      "LiteSpeed serves many PHP/CMS stacks similarly: vhosts, PHP handlers, cache, TLS. If you inherit a LiteSpeed box, map the same questions — where is the docroot, where are error logs, how is PHP run — even if the admin UI differs from Nginx.",
      "Speak concepts first; don't invent panel click-paths you don't remember.",
      "LiteSpeed serve nhiều stack PHP/CMS tương tự: vhost, PHP handler, cache, TLS. Inherit máy LiteSpeed thì hỏi cùng câu — docroot đâu, error log đâu, PHP chạy thế nào — dù UI admin khác Nginx.",
      "Nói khái niệm trước; không bịa click-path panel không nhớ.",
      "Claiming deep LiteSpeed tuning without one concrete change is fluff."),

    C("sec-web", "502 / 504 quick read", "Upstream vs edge",
      "502/504 often mean the proxy can't reach PHP-FPM/app or the upstream timed out. Check upstream socket/port, service status, and app fatals in logs — not only Nginx status.",
      "Cloud Run equivalent: revision crash or upstream SQL timeout shows in Cloud Logging.",
      "502/504 thường là proxy không tới được PHP-FPM/app hoặc upstream timeout. Check upstream socket/port, status service, và fatal app trong log — không chỉ status Nginx.",
      "Tương đương Cloud Run: revision crash hoặc SQL timeout hiện trên Cloud Logging.",
      "reload nginx alone rarely fixes a dead PHP-FPM."),

    # ── sec-security ──────────────────────────────────────────────────────────
    C("sec-security", "Secrets handling", "Out of Git, least readers",
      "Store credentials in Secret Manager or CI secret stores. Inject at runtime into Cloud Run or the VM env. Restrict who and which service accounts can read.",
      "Rotate after leak suspicion; don't just delete the chat message that had the password.",
      "Giữ credential trong Secret Manager hoặc secret CI. Inject runtime vào Cloud Run hoặc env VM. Restrict ai và SA nào được đọc.",
      "Rotate khi nghi leak; không chỉ xóa tin nhắn chat có password.",
      "Screenshots of .env in tickets are still leaks."),

    C("sec-security", "Least privilege", "IAM and OS",
      "Grant the minimum roles for Cloud Build to push/deploy and for the app SA to read its secrets/SQL. On Linux, separate sudo users and tight file ownership for the web root.",
      "Owner/Editor for every engineer 'for speed' becomes the incident story.",
      "Cấp tối thiểu role để Cloud Build push/deploy và SA app đọc secret/SQL. Trên Linux: tách sudo user và ownership chặt cho web root.",
      "Owner/Editor cho mọi engineer 'cho nhanh' sẽ thành câu chuyện incident.",
      "Shared root password in a spreadsheet fails any serious interview."),

    C("sec-security", "SSH & network surface", "Close what you don't need",
      "Key-only SSH, limited VPC firewall / UFW ports (22 carefully, 80/443 for web), no public MySQL. Prefer bastion/IAP patterns when the team has them.",
      "Every open port is an assumption you must defend.",
      "SSH chỉ key, VPC/UFW limit port (22 thận trọng, 80/443 cho web), không MySQL public. Ưu tiên bastion/IAP nếu team có.",
      "Mỗi port mở là assumption bạn phải defend được.",
      "Temporary 0.0.0.0/0 rules that never expire are not temporary."),

    C("sec-security", "Hardening + docs", "Practical maturity",
      "Hardening is useless if only one person knows the server. Pair basic controls (SSH, firewall, secrets, patches) with short runbooks: deploy steps, log locations, TLS renew, rollback.",
      "I'm honest: practical hardening and documentation — not claiming a full formal audit program unless I've done one.",
      "Harden vô ích nếu chỉ một người biết server. Ghép control cơ bản (SSH, firewall, secret, patch) với runbook ngắn: bước deploy, chỗ log, renew TLS, rollback.",
      "Tôi nói thẳng: harden thực tế và docs — không claim chương trình audit formal nếu chưa làm.",
      "Security theater checklists nobody follows don't count."),
]
