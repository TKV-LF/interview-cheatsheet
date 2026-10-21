"""Speakable Vietnamese for the Go1 leadership scripts we kept."""

GO1_VI = {
    "q1": (
        "Hãy giới thiệu về bản thân.",
        "<p>Tôi là Thùy, backend và full-stack khoảng năm năm. Phần lớn việc là TypeScript, Node.js, PHP, API, database, và đưa sản phẩm lên production — CI/CD và cloud, không chỉ mỗi feature.</p><p>Gần đây tôi làm việc khách hàng và với Akktis, công ty ở Pháp. Việc đổi nhiều, nên tôi quen nhận một hệ thống mới, hỏi đúng câu, và chịu đường từ build tới deploy tới support.</p><p>Dự án tôi tâm nhất là IELTS AI Tutor — đã lên Play Store và App Store, khoảng 5.000 người dùng, tăng khoảng 900 đến 1.000 mỗi tháng. Lúc đầu backend và web của tôi mạnh hơn mobile và CI/CD. Tôi dùng LLM để học React Native, bản store, và pipeline, rồi vẫn phải hiểu và tự ship. Tôi cũng làm phần AI trong sản phẩm — chat, text-to-speech, speech-to-text — và dùng Langfuse để thấy model thực sự trả gì.</p><p>Trước đó ở BaseVN tôi làm SaaS HR, payroll và tuyển dụng lớn. Tôi học được data thật rối thế nào khi nhiều hệ thống phải khớp nhau.</p><p>Tôi muốn một product team nơi tôi tiếp tục làm phần mềm học tập hữu ích, làm với kỹ sư khác, và đi sâu các tính năng AI phải đáng tin với người dùng thật.</p>",
    ),
    "q3": (
        "Kể lần bạn phải học cái mới, hoặc thu thêm thông tin, thì mới tiến được.",
        "<p>Ví dụ rõ là IELTS AI Tutor. Cần một sản phẩm thật: app React Native trên iOS và Android, luồng giáo viên, backend trên Cloud Run, và cách build rồi phát hành. Thật ra lúc đầu mobile của tôi không sâu, và tôi cũng mới với CI/CD kiểu này — bản store, môi trường, deploy Cloud Run.</p><p>Tôi đã có backend và web, nên không phải từ số không. Nhưng tôi không thể chờ đến khi thấy mình là chuyên gia mobile. Tôi dùng LLM như một phần cách làm: nhờ giải thích pattern React Native và Expo, draft config pipeline, và gỡ lỗi tôi chưa gặp. Phần model không làm được là của tôi: chạy thật, đọc docs khi câu trả lời có vẻ sai, test trên máy thật, và chỉ giữ cái tôi hiểu.</p><p>Tôi học từng lát. Một màn hình chạy được. Rồi điều hướng và auth. Rồi nối API. Rồi pipeline để không ai phải bấm phát hành tay. Chat, TTS, STT cũng vậy: test nhỏ, rồi Langfuse, vì API 200 vẫn có thể là một bài học tệ.</p><p>Kết quả là app sống trên Google Play và App Store, backend deploy và debug được. Bài học: kỹ năng mới không có nghĩa là giấu chỗ hổng. Tôi dùng mọi tool, kể cả LLM, rồi chịu trách nhiệm cái được ship.</p>",
    ),
    "q4": (
        "Bạn đã cải thiện hiệu suất, tinh thần, hiệu quả, hoặc hướng đi của team thế nào?",
        "<p>Một số dự án, các bước deploy nằm trong đầu một người. Release chậm, và nếu người đó vắng thì support khó.</p><p>Tôi không phải manager. Tôi bắt đầu từ nỗi đau: sót bước, rối môi trường, troubleshoot lâu. Tôi viết lại luồng hiện tại, rồi làm pipeline lặp lại được — GitHub Actions, GitLab CI hoặc Jenkins tùy dự án — với Docker và Cloud Run ở chỗ dùng. Tôi ghi thứ tự build, config env, và kiểm gì sau deploy.</p><p>Kết quả không chỉ là release nhanh hơn. Người khác ship và debug được mà không chờ một người. Tôi không có số phút tôi tin. Cái đổi là ownership: trước đó bước deploy nằm trong một cái đầu; sau đó pipeline là nguồn sự thật và ai trong team cũng ship được.</p>",
    ),
    "q5": (
        "Kể một mục tiêu khó, hoặc lúc bạn thấy kẹt, và cách đi tiếp thực tế.",
        "<p>Ở BaseVN tôi làm hệ thống HR, payroll, thuế và bảo hiểm. Một số luồng ngồi trên hơn 500.000 bản ghi, và data đi giữa các hệ thống.</p><p>Tôi thấy kẹt vì không phải một query chậm. Phải biết hệ nào là nguồn sự thật, bản ghi thiếu hoặc trùng sẽ làm gì với payroll hoặc report, và thay đổi nào là an toàn.</p><p>Tôi làm bài toán hiện ra trước. Tôi vẽ luồng data, đánh dấu entity quan trọng, xem schema và query hiện tại, và bắt đầu từ đường rủi ro cao — đường có thể làm hỏng tiền hoặc báo cáo tuân thủ — không phải refactor dễ nhất.</p><p>Từ đó tôi cải thiện cấu trúc và query từng bước, không viết lại tất cả. Bài học: khi hệ thống quá lớn, tôi cần bức tranh phụ thuộc trước khi đụng đường data production.</p>",
    ),
    "q6": (
        "Kết quả ngắn hạn và kết quả dài hạn. Và lần bạn theo một kế hoạch bạn không đồng ý lúc đầu.",
        "<p>Tôi không coi đây là \"ship rác bây giờ\" đối \"xây hệ thống hoàn hảo\". Tôi chia hai danh sách. Tôi sẽ cắt cho bản đầu: tính năng thêm, trợ lý AI rộng, polish, và viết lại lớn không đổi được việc user làm tuần này. Tôi không cắt: độ đúng của data, bảo mật — key ở server — xử lý lỗi cơ bản, deploy rollback được, và cách biết tính năng có thật sự chạy. Đó không phải \"để sau cho đẹp\". Bỏ chúng thì thắng ngắn hạn thành cháy dài hạn.</p><p>IELTS AI Tutor là ví dụ. Áp lực ngắn hạn là có app thật trên store, học viên dùng được. Trợ lý \"làm mọi thứ\" sẽ lâu hơn, và ta không biết đó là bài học tốt hay chỉ là HTTP 200. Kết quả ngắn hạn là một luồng hẹp hơn: ship đường luyện cốt lõi. Khoảng 5.000 người dùng, tăng 900 đến 1.000 mỗi tháng — chỉ có nếu ship. Phần dài hạn tôi vẫn đặt từ ngày đầu: điện thoại không giữ key OpenAI; chat, TTS, STT đi qua Express; có fallback; Langfuse để câu lạ là một trace. CI/CD và Cloud Run cũng nằm trong danh sách không bỏ.</p><p>Với Base PIT, nếu họ hỏi ví dụ khác: ngắn hạn là kịp ngày launch với file export khách cần. Dài hạn là không để file thuế nhanh mà sai. Chúng tôi ship export hiện tại, nhưng tôi vẫn thêm index, chia batch, và một sample đã biết để Excel/XML khớp HRM và Payroll.</p><p>Lần tôi không đồng ý lúc đầu: quanh launch PIT tôi muốn đưa export Excel/XML nặng ra khỏi request — job nền rồi mới tải — vì đã hơn 500.000 bản ghi. Tôi sợ kỳ thuế đầu trên công ty lớn bị timeout, hết memory, hoặc tệ hơn, ra file trông ổn nhưng sai. Product owner và tech lead vẫn chọn ship export hiện có để kịp ngày. Tôi theo. Tôi không cãi tiếp. Tôi làm kế hoạch của họ an toàn nhất có thể: tìm query chậm, sửa index, bỏ SELECT * và N+1, xử lý theo lô, giữ sample nhỏ để file vẫn khớp. Tôi ghi rủi ro còn lại: đường job vẫn là bước đúng tiếp theo. Launch xong, khách đầu export được. Bài học: tôi đẩy một lần, rõ, rồi giúp team thắng. Tôi chỉ leo lại nếu bảo mật, tiền, hoặc người dùng thật sự nguy.</p>",
    ),
    "q7": (
        "Vì sao nên tuyển bạn?",
        "<p>Tôi đã làm trong stack này — TypeScript, Node, PHP, API — và đã ship cả UI lẫn service, gồm SaaS. Tôi quen cả đường: build, test, deploy, và debug trên production.</p><p>Tôi làm được khi yêu cầu chưa rõ. Việc khách hàng hiếm khi spec đủ. Tôi hỏi ít câu, viết giả định, và kiểm bằng bản nhỏ thay vì chờ spec hoàn hảo.</p><p>Tôi cũng đã dùng LLM theo cách vai này cần. Với IELTS tôi không phải chuyên gia mobile hay CI/CD từ ngày đầu. Tôi dùng AI để học và ship, rồi vẫn chịu bản store và lỗi production. Tôi không phải kỹ sư nghiên cứu. Tôi học nhanh, ship, và giữ kết quả đáng tin.</p>",
    ),
    "q8": (
        "Yêu cầu không rõ thì bạn làm gì?",
        "<p>Việc khách hàng hay vậy. Họ biết mục tiêu nghiệp vụ — luồng giáo viên và học viên — nhưng vai, quyền, và case lỗi chưa được viết.</p><p>Tôi không bắt đầu bằng code cả thứ. Tôi tách luồng user chính, data, tích hợp, và phần sẽ đau sau. Rồi tôi hỏi một danh sách ngắn và nói giả định thành lời. Nếu cần tôi vẽ luồng đơn giản hoặc làm bản mỏng đầu tiên.</p><p>Người ta thường biết vấn đề. Họ cần giúp biến nó thành workflow làm được.</p>",
    ),
    "q9": (
        "Bạn gây ảnh hưởng khi không phải manager thế nào?",
        "<p>Cùng chuyện pipeline deploy. Câu cuối khác: tôi đề xuất một thay đổi nhỏ, dễ nhận, và nói lợi ích bằng ngôn ngữ của họ — ít sai hơn, ít phải chờ một người hơn.</p>",
    ),
    "q10": (
        "Ownership nghĩa là gì với bạn? Kể một ví dụ.",
        "<p>IELTS không phải một ticket, và tôi chưa phải chuyên gia mobile hay CI/CD khi bắt đầu. Tôi vẫn chịu cả đường: app React Native, nối cổng giáo viên, Express trên Cloud Run, phát hành store, và phần AI. Tôi dùng LLM để học nhanh hơn, nhưng lỗi sau release vẫn là việc của tôi — build fail hoặc câu trả lời tutor lạ.</p><p>Langfuse là một phần ownership. Nếu không thấy user nhận được gì, ta không support được sản phẩm. Tôi hay hỏi: nó chạy không, fail thì sao, và tháng sau debug thế nào?</p>",
    ),
    "q11": (
        "Bạn quyết khi thông tin chưa đủ thế nào?",
        "<p>Tôi tách quyết định. Nếu sau này đổi dễ, tôi giả định hợp lý, viết ra, test, và đi tiếp. Nếu khó đảo — data production, bảo mật, một lựa chọn kiến trúc lớn — tôi chậm lại.</p><p>Tôi nói cái tôi biết, cái tôi đang giả định, rủi ro, và tôi sẽ kiểm gì tiếp. Như vậy team đi tiếp mà không giả vờ chắc chắn.</p>",
    ),
    "q12": (
        "Kể một lần bạn bất đồng.",
        "<p>Một lần đẩy production tối thứ Sáu ở Akktis. PM phía khách muốn thay đổi lên trong buổi tối. Phía họ hợp lý: khách đang chờ, diff trông nhỏ, thêm một cuối tuần là trượt lời hứa. Một kỹ sư khác sẵn sàng ship.</p><p>Tôi không thoải mái. Chúng tôi khác múi giờ. Nếu bỏ staging và có gì gãy sau khi châu Âu offline, tôi là người trên máy, và rollback sẽ rối. Nỗi sợ không phải \"quy trình cho có quy trình\". Là một sự cố Chủ nhật khi không còn ai biết thay đổi đó online.</p><p>Tôi không biến thành chuyện cá nhân. Tôi nói lại mục tiêu của họ — khách phải nhận được bản sửa — rồi nói rủi ro: lệch env, sót biến, không rollback sạch. Tôi xin đường giữa: một lượt staging ngắn, rollback viết ra, rồi deploy. Chúng tôi làm vậy. Thay đổi vẫn lên trong ngày, sau một lần kiểm staging. Nó đứng. Sau đó PM vẫn đẩy ngày — đó là việc của họ — nhưng họ bắt đầu hỏi ghi chú rollback. Vẫn làm việc với nhau được. Dễ với người, cứng với cách deploy.</p>",
    ),
    "q13": (
        "Bạn làm việc qua quốc gia và múi giờ thế nào?",
        "<p>Với Akktis và khách tôi làm khác múi giờ. Tôi không thể trông vào một cuộc họp nhanh để sửa mọi thứ.</p><p>Tôi viết cập nhật chạy được khi async: tôi đã làm gì, cái gì bị kẹt, tôi cần gì, bước tiếp là gì. Tôi ghi quyết định kỹ thuật để người offline vẫn có ngữ cảnh. Tôi không giả định chung ngữ cảnh, nhất là với khách.</p><p>Điều đó làm tôi tự lập hơn, và cũng cẩn thận hơn: nếu người ta không thấy việc, việc chưa xong.</p>",
    ),
    "q14": (
        "Nhận feedback, điểm yếu, và một lỗi bạn đã mắc.",
        "<p>Điểm yếu: tôi thoải mái khi tự điều tra. Đôi khi tôi chờ quá lâu mới chia sẻ tiến độ hoặc rủi ro. Tôi đang tập cập nhật sớm hơn: cái tôi biết, cái tôi còn đang kiểm, cái tôi cần. Tôi vẫn làm độc lập mà không để team trong bóng tối. Chuyện này càng quan trọng trên team remote.</p><p>Một lỗi: trước đây tôi đôi khi xây cái đúng về kỹ thuật trước khi workflow nghiệp vụ rõ — vai, edge case, ai được làm gì. Bây giờ tôi xác nhận sớm: giả định, sơ đồ đơn giản, bản mỏng. Nhanh không chỉ là tốc độ gõ. Là giải đúng bài.</p>",
    ),
    "q17": (
        "Leadership và sự tò mò nghĩa là gì với bạn?",
        "<p>Với một IC, leadership là giúp nhóm đi tới. Rõ ràng, rủi ro nhìn thấy được, nhận việc khi mọi thứ còn mờ, và quan tâm kết quả đầy đủ — đáng tin, hiểu được, hữu ích — không chỉ \"PR của tôi đã qua\". Tôi thể hiện bằng việc làm, bằng cách viết, và bằng quy trình tôi để lại.</p><p>Tò mò: tôi không dừng ở câu trả lời đầu. Tôi muốn biết vì sao nó gãy, user đang cố làm gì, và ta đang đánh đổi gì. Trên một product team điều đó còn là hỏi ngoài một ticket hẹp, rồi đặt cái đã học lại trước team.</p>",
    ),
    "q19": (
        "Vì sao vai này, vì sao lúc này? Bạn làm việc với product và design thế nào?",
        "<p>Vì sao lúc này: tôi muốn đứng gần một sản phẩm hơn và đi sâu phần học tập có AI, thay vì chỉ nhảy giữa các stack khách hàng.</p><p>Với product và design: tôi học việc của user trước. Tôi hỏi thế nào là thành công, đo gì, và edge case nào sẽ sinh tải support. Tôi nói giới hạn kỹ thuật sớm — độ trễ, chi phí, quyền — để không thiết kế một luồng hệ thống không giữ được. Nếu chưa rõ, tôi thích một bản nhỏ cùng bấm qua.</p>",
    ),
    "q21": (
        "90 ngày đầu bạn sẽ làm gì?",
        "<p>Tháng đầu: học sản phẩm, codebase, cách team ship, và cách làm việc với product ở múi giờ khác. Tôi thà hỏi câu \"ngớ ngẩn\" sớm còn hơn âm thầm xây sai. Ship một thứ nhỏ và an toàn, có test và PR sạch, để người ta tin việc của tôi.</p><p>Tháng hai và ba: nhận một lát thật — một feature hoặc một cải thiện reliability — và để đường đi rõ hơn lúc tôi tới. Docs, một check trong CI, hoặc cách thấy câu trả lời AI có thật sự hữu ích. Tôi cũng theo workflow LLM team đang dùng, thay vì tự bịa một cái.</p>",
    ),
    "q22": (
        "Ưu tiên đổi giữa chừng. Và lần bạn làm ngoài mô tả công việc.",
        "<p>Ưu tiên: tôi kiểm lại impact và khả năng đảo ngược. Cái gì user thấy hoặc nguy nếu tạm dừng? Cái gì chờ được? Tôi nói cái tôi sẽ dừng, không chỉ cái tôi sẽ bắt đầu, để không có việc chết thầm.</p><p>Ngoài việc được giao: CI/CD và tài liệu khi \"không phải ticket của tôi\", và Langfuse khi nhu cầu là \"ta không thấy AI\". Tôi làm khi nó mở đường cho team hoặc user, rồi nói cho mọi người để nó không thành việc vô hình.</p>",
    ),
    "q24": (
        "Đi qua IELTS AI Tutor.",
        "<p>Đó là app React Native TypeScript cho iOS và Android, đã lên cả hai store, cộng cổng giao bài cho giáo viên. Khoảng 5.000 người dùng, tăng khoảng 900 đến 1.000 mỗi tháng. Tôi làm app mobile, API Express trên Cloud Run, và cầu giữa phía học viên và giáo viên.</p><p>Tôi nên nói thẳng: lúc bắt đầu backend và web của tôi mạnh hơn mobile và CI/CD. Tôi dùng LLM để học Expo và React Native, bản store, và pipeline, rồi tự kiểm mọi thứ. AI cũng nằm trong sản phẩm — chat, TTS, STT — với Langfuse cho trace. Firebase là một phần setup.</p><p>Phần thú vị không phải là gọi một API. Là học đủ để ship app thật, rồi nghĩ về thời gian chờ, lỗi, và cách điều tra một câu trả lời tệ sau này.</p>",
    ),
    "q25": (
        "Bạn thiết kế một tính năng học bằng AI thế nào? Ảo giác và cách đánh giá?",
        "<p>Thiết kế: bắt đầu từ việc của người học — hiểu, luyện, nhận góp ý, hoặc tìm khóa. Ship một case đầu hẹp. Rồi auth, quyền, validation, rate limit, log, fallback. Nếu có nội dung đã duyệt, lấy nội dung đó và giữ model trong cái hộp ấy. Đo độ trễ, lỗi, chi phí, và người học có tiếp tục không.</p><p>Ảo giác: không chỉ là prompt hay hơn. Đưa nội dung tin được, ràng output, cho phép \"tôi không biết\", và fallback sang catalog hoặc người. Xem trace thật. Vì vậy tôi dùng Langfuse.</p><p>Đánh giá: sức khỏe kỹ thuật cộng chất lượng sản phẩm. Một 200 nhanh vẫn có thể là bài vô ích hoặc sai. Tôi muốn câu hỏi vàng, người review, và hành vi sau release: hỏi lại, bỏ giữa chừng, kiểu thumbs-down.</p>",
    ),
    "q28": (
        "Sự cố production, CI/CD, và cách bạn dùng LLM khi làm việc.",
        "<p>Production: impact trước. Ổn định — rollback, workaround, hoặc tắt — rồi nguyên nhân: thay đổi gần, log, config, dependency, tài nguyên. Sau đó một ngăn nhỏ: monitor, check CI, hoặc docs. Tôi không vá ngẫu nhiên khi đang căng.</p><p>CI/CD: GitHub Actions, GitLab CI, Jenkins, Docker, Linux, Cloud Run và Cloud Storage. Pipeline nên build, kiểm, deploy, và báo service có khỏe không. Rollback và secret là một phần thiết kế.</p><p>LLM hằng ngày: trên IELTS tôi dùng để học React Native và CI/CD — draft màn hình, một lỗi chưa gặp, một đoạn pipeline — rồi tôi chạy build, đọc diff, và chỉ giữ cái tôi hiểu. Trong sản phẩm tôi coi model là thành phần không đáng tin: key ở server, log bằng Langfuse, và có fallback. Dùng AI để đi nhanh hơn, không bỏ phán đoán.</p>",
    ),
    "cv-map": (
        "Nếu họ chỉ vào dòng này trên CV, bạn kể chuyện nào?",
        "<p>Base PIT, hơn 500.000 bản ghi, schema, query, Excel/XML, launch: họ hỏi tối ưu thế nào, cái gì chậm — kể thuế và report, độ đúng quan trọng hơn tốc độ.</p><p>Base VSS, sync HRM và Payroll, Excel/XML: bug data khó nhất, lệch thầm — nguồn sự thật.</p><p>E-Hiring, VietnamWorks và TopCV: API bên thứ ba không ổn — retry, log, monitoring.</p><p>Akktis, Linux, CI/CD, Cloud Run và SQL: sự cố production — lệch env, đầy đĩa, không nối được DB.</p><p>Legacy sang MySQL trên Apache: cutover khó, sợ mất data — backup, kiểm, viết lại.</p><p>IELTS, React Native, Express, Cloud Run, Langfuse: bug AI qua được demo — trace, không chỉ HTTP 200.</p>",
    ),
    "cv-500k": (
        "Bạn viết đã tối ưu query cho hơn 500.000 bản ghi. Kể lại.",
        "<p>Base PIT là sản phẩm thuế thu nhập cá nhân. Hơn 500.000 bản ghi, phải nói chuyện với HRM và Payroll. Chỗ đau là report và export — Excel và XML cho tuân thủ — cộng các màn load hoặc lọc nhiều dữ liệu nhân viên và kỳ.</p><p>Luật đầu: tôi không chạy report 500.000 dòng trong một request của user. Sẽ timeout hoặc hết memory. Export và sync nặng là đường job: cắt việc, ghi file, rồi user tải.</p><p>Rồi tôi tìm query chậm thật. Slow query log hoặc query sau màn hình chậm, chạy EXPLAIN, xem full scan, join xấu, hoặc thiếu index trên cột thật sự lọc — công ty, nhân viên, kỳ. Tôi cũng tìm SELECT * và N+1.</p><p>Cái tôi đổi thường nhàm và an toàn: index khớp WHERE và JOIN, viết lại query chỉ lấy cột và dòng report cần, xử lý theo lô thay vì nhét cả bảng vào memory PHP. Đôi khi schema là vấn đề — kiểu, khóa, bảng gộp quá nhiều việc — tôi sửa cẩn thận và test lại export.</p><p>Tôi luôn kiểm độ đúng, không chỉ tốc độ. Với data thuế tôi so một sample nhỏ đã biết: cùng nhân viên, cùng kỳ, Excel/XML vẫn khớp HRM và Payroll. Nhanh mà sai là launch tệ hơn chậm mà đúng.</p>",
    ),
    "cv-explain": (
        "Bạn tìm query chậm thế nào? EXPLAIN cho biết gì?",
        "<p>Tôi bắt đầu từ triệu chứng của user: màn nào, export nào, công ty và kỳ nào. Rồi tôi lấy SQL — từ log, từ ORM, hoặc bằng cách làm lại thao tác. Tôi chạy EXPLAIN.</p><p>Tôi tìm type ALL hoặc rows rất lớn, không có key hữu ích, hoặc join nổ. Thường là thiếu index hoặc filter không dùng được index — hàm bọc cột, sai kiểu, hoặc SELECT * cộng sort cả bảng.</p><p>Tôi đổi một thứ, đo lại, và giữ bản query cũ. Tôi không \"chỉnh production\" bằng cách đoán.</p>",
    ),
    "cv-paginate": (
        "Bạn có trả 500.000 dòng về API hoặc điện thoại không?",
        "<p>Không. Danh sách trên điện thoại hoặc bảng web cần phân trang và chỉ các field màn hình cần. File thuế đầy đủ là export nền, không phải một cục JSON. Cùng ý tôi dùng trên IELTS: tôi không hydrate payload khổng lồ mỗi topic nếu có thể giữ progress tại chỗ và lấy đúng phần màn hình cần.</p>",
    ),
    "cv-caught": (
        "Vấn đề quan trọng nhất bạn bắt được, và bạn sửa thế nào?",
        "<p>Loại vấn đề quan trọng nhất tôi từng bắt là lệch data thầm, không phải một crash.</p><p>Trên Base VSS chúng tôi sync dữ liệu bảo hiểm xã hội với HRM và Payroll, và export Excel/XML. Crash thì thấy ngay. Sync \"thành công\" nhưng map sai thì tệ hơn — số đếm trông ổn đến khi tài chính hoặc đường thuế nhận ra.</p><p>Cách bắt: tôi không tin log success của job. Tôi lấy sample nhỏ đã biết — vài nhân viên kiểm tay được — và so field nguồn với đích với file export. Tôi kiểm thứ tự job: Payroll đọc trước khi HRM xong thì ra sự thật của hôm qua.</p><p>Cách sửa: đúng mapping hoặc luật biến đổi, hoặc thứ tự job, rồi thêm bước kiểm rõ hơn — đếm dòng, field bắt buộc, hoặc kiểm kiểu checksum trên sample — để lần sau lỗi phải ồn. Rồi chạy lại sample trước khi đụng full set.</p>",
    ),
    "cv-hardest": (
        "Việc khó nhất bạn từng làm là gì?",
        "<p>Khó nhất là Base PIT quanh launch. Không phải một query chậm. Data lớn, report phải đúng, Excel/XML phải khớp HRM và Payroll, và có deadline. Tối ưu nhầm đường thì export nhanh mà số thuế sai.</p><p>Khó vì các mối nối. Tôi phải thấy luồng trước: hệ nào là nguồn sự thật, query nào nằm trên đường launch, bản ghi trùng hoặc thiếu làm gì với report. Rồi tôi bắt đầu từ đường rủi ro cao — tiền và tuân thủ — không phải refactor dễ.</p><p>Cách đi: vẽ, đo, đổi một lớp, kiểm bằng sample đã biết, rồi lớp tiếp. Tôi vẫn dùng cách đó khi một hệ thống cảm giác quá lớn.</p><p>Khó thứ hai, nếu họ hỏi thêm: migrate legacy ở Akktis khỏi DB tùy biến. Nỗi sợ là mất data, không phải cú click. Backup và nghĩ rollback, kiểm đọc/ghi sau cutover, viết đường Apache/MySQL mới để support không nằm trong đầu một người.</p>",
    ),
    "cv-estimate": (
        "Bạn ước lượng thời gian một task thế nào?",
        "<p>Tôi không ước lượng một ticket mờ thành một con số. Tôi tách trước.</p><p>Một: cái đã rõ — màn hình, API, query tôi đã thấy. Hai: cái chưa biết — khối lượng data, API bên thứ ba, chưa có quyền vào env, luật chưa rõ. Ba: test và release — nhất là khi đụng thuế, sync, hoặc data production.</p><p>Phần đã biết tôi ước từ việc tương tự. CRUD thường là một chuyện. Report kiểu PIT trên bảng lớn là chuyện khác, vì cần thời gian profile, index, và kiểm sample. Tích hợp kiểu VietnamWorks cần thời gian cho auth, retry, và đường response lỗi, không chỉ JSON hạnh phúc.</p><p>Tôi nói giả định thành lời: ba ngày nếu mapping có tài liệu và tôi dùng được dump staging. Nếu dump rối hoặc API vendor khác docs, tôi cần nửa ngày spike và ước lại. Tôi thêm buffer cho lát rủi ro, không nhân đôi thầm mọi thứ. Nếu task lớn hơn, tôi nói sớm. Bất ngờ muộn tệ hơn một ước lượng sửa vào ngày đầu.</p>",
    ),
    "cv-estimate-wrong": (
        "Ước lượng sai thì sao? Bạn bẻ một task lớn thế nào?",
        "<p>Nếu tôi trượt, tôi không âm thầm làm khuya và hy vọng. Tôi nói cái đã xong, cái bị kẹt, và ngày mới kèm lý do — export cần chia chunk, spec không cho thấy điều đó.</p><p>Với task lớn tôi cắt một lát dọc mỏng demo được: một công ty, một kỳ, một export, hoặc một luồng học viên. Phần còn lại là việc tiếp. Đó là cách giữ tốc độ mà không giấu nợ.</p><p>Ví dụ PIT: tôi không ước \"tối ưu cả database\". Tôi ước \"export theo kỳ chạy xong và khớp một sample\", rồi lát tiếp cho report tiếp theo.</p>",
    ),
    "cv-priority": (
        "Nhiều thứ cùng chậm hoặc cùng hỏng, bạn sửa cái nào trước?",
        "<p>Impact và khả năng đảo. User bị kẹt hoặc data sai đi trước. Rồi report trên đường launch. Rồi tốc độ cho đẹp.</p><p>Trên PIT, XML sai cho cơ quan thuế nặng hơn một trang danh sách hơi chậm. Trên IELTS, STT fail chặn luyện nói nặng hơn animation chậm. Trên server, đĩa đầy hoặc Cloud SQL không tới được nặng hơn một lỗi style.</p>",
    ),
    "cv-sync": (
        "Kể một bug sync. API bên thứ ba. Rủi ro migrate.",
        "<p>Sync VSS: lệch thầm. Làm lại trên tập nhỏ đã biết, so nguồn với đích, kiểm biến đổi và thứ tự job, sửa mapping, thêm validation, rồi mới chạy full.</p><p>E-Hiring, VietnamWorks, TopCV: lỗi là rate limit, auth hết hạn, hoặc response đổi. Tôi làm lỗi ồn: retry chỗ an toàn, request id trong log, monitor job sync. Tôi không giả vendor luôn sống.</p><p>Legacy sang MySQL/Apache: phần khó là sự tin. Backup và rollback trước. Sau cutover tôi kiểm app đọc và ghi được. Tôi viết đường mới để người sau không phải đoán.</p>",
    ),
    "cv-prod": (
        "Một sự cố production bạn đã sửa. Một thứ bạn bắt ở staging.",
        "<p>Staging xanh, prod đỏ: tôi so commit, biến env, secret, và phiên bản service trước khi sửa code. Thường là thiếu biến, config web server khác, hoặc dependency chỉ cài một môi trường. Sửa config, deploy lại, thêm vào checklist.</p><p>Cloud Run lên, DB xuống: log, rồi connection string, rồi mạng hoặc socket, rồi quyền service account. Thường là identity hoặc host, không phải \"Node chết\".</p><p>Đĩa Linux đầy: df và du, giải phóng an toàn, xoay log, restart service, rồi làm đĩa hiện trên monitoring. Tôi không xóa mù dưới /var.</p><p>Pipeline đỏ giữa release: dừng retry spam. Đọc stage nào fail. Sửa nhỏ nhất. Chỉ promote khi xanh. Rồi làm lỗi đó ồn sớm hơn.</p>",
    ),
    "cv-test": (
        "Bạn test một report, một export, hoặc một đổi schema thế nào?",
        "<p>Tôi giữ một fixture: một công ty nhỏ hoặc vài nhân viên có số tôi đã biết. Tôi chạy đường cũ và đường mới rồi so. Với Excel/XML tôi kiểm tổng và vài dòng, không chỉ \"file đã tải\".</p><p>Với đổi schema hoặc index tôi kiểm cả đường ghi — insert và job sync — vì index mới có thể làm chậm ghi. Rồi tôi chạy export nặng một lần trên volume thật nếu có dump staging, không phải lần đầu trên production.</p>",
    ),
    "cv-leave": (
        "Vì sao bạn rời BaseVN? Điểm mạnh kỹ thuật lớn nhất trên CV là gì?",
        "<p>Vì sao rời BaseVN: tôi may — không chỉ viết ticket. Tôi đứng gần sản phẩm, gần như product owner phía HRM. Tôi xây feature và hiểu vì sao chúng quan trọng với khách. Đó là nền tốt.</p><p>Trong thời gian tôi ở đó, hướng công ty tập trung hơn vào dòng sản phẩm khác. Bộ HRM tôi làm còn ít chỗ để lớn. Đồng thời tôi muốn thử môi trường khác — outsourcing toàn cầu, khách quốc tế, cách làm khác. Vì vậy tôi sang Akktis.</p><p>Khoảng hai năm ở Akktis tôi học nhiều: Linux, CI/CD, cloud, giao hàng cho khách qua múi giờ. Nhưng tôi cũng nhận ra điều tôi nhớ. Tôi muốn xây sản phẩm lại — gần user, làm với product và design, chịu kết quả theo thời gian, không chỉ dự án nối dự án.</p><p>Điểm mạnh kỹ thuật lớn nhất: tôi đi một vấn đề xuyên các lớp và vẫn quan tâm kết quả sản phẩm. Màn thuế chậm có thể là query, thiếu index, hoặc job không nên nằm trong request. Câu AI lạ có thể là model hoặc workflow. Tôi debug bằng bằng chứng — EXPLAIN, log, Langfuse — rồi để đường đi rõ hơn cho người sau.</p>",
    ),
    "cv-pokes": (
        "Các câu chọc CV khác — mỗi câu một lời 30 giây.",
        "<p>Đi qua CV: mới nhất trước. Akktis và IELTS, rồi quy mô BaseVN.</p><p>E-Hiring: sync VietnamWorks và TopCV, report và Excel, theo dõi email. Có kế hoạch retry.</p><p>LiteSpeed và Apache: vhost, hiệu năng cơ bản, tách \"HTTP sai\" khỏi \"app sai\".</p><p>IAP và webhook IELTS: điện thoại không giữ key OpenAI. Mua hàng và AI đi qua Express trên Cloud Run.</p><p>Vì sao Langfuse: HTTP 200 không phải một bài học tốt. Trace cho thấy user nhận được gì.</p><p>Looneyes và Jimdo: giữ ngắn. Ownership khách thật, không phải phần hệ thống sâu nhất.</p><p>Vào codebase lớn: chạy lên, tìm đường request, tìm data model, hỏi ai giữ production.</p>",
    ),
}
