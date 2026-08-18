"""Build six missing translated common-scam guide hubs.

The pages are intentionally static and self-contained so they can be served by
GitHub Pages and discovered through the existing sitemap and RSS feed.
"""
from datetime import datetime, timedelta, timezone
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://alphaengineerai.com/"
SHIELD = "https://minddividend-shield.joe303262000.chatgpt.site/"
STAMP = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")

LANGUAGE_LINKS = [
    ("English", "common-online-scams.html"),
    ("Español", "estafas-online-comunes.html"),
    ("Português", "golpes-online-comuns.html"),
    ("Français", "arnaques-en-ligne-courantes.html"),
    ("Deutsch", "online-betrugsmaschen.html"),
    ("हिन्दी", "online-scam-guide-hi.html"),
    ("العربية", "online-scam-guide-ar.html"),
    ("繁體中文", "common-online-scams-zh-hant.html"),
    ("Bahasa Indonesia", "common-online-scams-id.html"),
    ("Tiếng Việt", "common-online-scams-vi.html"),
    ("日本語", "common-online-scams-ja.html"),
    ("한국어", "common-online-scams-ko.html"),
    ("Italiano", "common-online-scams-it.html"),
]

ALTERNATES = [
    ("en", "common-online-scams.html"),
    ("es", "estafas-online-comunes.html"),
    ("pt-BR", "golpes-online-comuns.html"),
    ("fr", "arnaques-en-ligne-courantes.html"),
    ("de", "online-betrugsmaschen.html"),
    ("hi", "online-scam-guide-hi.html"),
    ("ar", "online-scam-guide-ar.html"),
    ("zh-Hant", "common-online-scams-zh-hant.html"),
    ("id", "common-online-scams-id.html"),
    ("vi", "common-online-scams-vi.html"),
    ("ja", "common-online-scams-ja.html"),
    ("ko", "common-online-scams-ko.html"),
    ("it", "common-online-scams-it.html"),
]

PAGES = {
    "common-online-scams-zh-hant.html": {
        "lang": "zh-Hant", "checker": "scam-message-checker-zh-hant.html", "campaign": "scams_zh_hant",
        "title": "常見網路詐騙：實用的初步辨識指南",
        "description": "辨識假銀行通知、包裹簡訊、工作邀請、投資話術、社群帳號冒用與假客服的詐騙警訊。",
        "hero1": "網路詐騙的故事不同。", "hero2": "施壓模式往往相同。",
        "dek": "這份實用指南協助你在點擊、付款、回覆或分享資料前，辨識銀行通知、包裹、工作、投資、社群帳號與假客服中的早期警訊。",
        "check": "檢查可疑訊息", "scenarios": "八種常見詐騙情境", "intro": "品牌和故事會因國家而變化，但要求你尚未查證就先行動的模式很相似。",
        "cards": [("假銀行通知", "緊急帳戶警告要求你透過連結登入、提供驗證碼，或為了「安全」把錢轉到另一個帳戶。"), ("假包裹通知", "訊息聲稱地址有問題或需要支付小額重新配送費，並把你帶到仿冒付款頁面。"), ("網路工作邀請", "對方承諾輕鬆賺取遠端收入，接著要求先付款、存入加密貨幣、提供證件或代收轉寄。"), ("投資或加密貨幣話術", "保證獲利、秘密群組、名人背書，以及要求不斷加碼，都是重要風險訊號。"), ("二手交易買家或賣家", "對方要求離開平台、提供假付款截圖、故意多付，或在交易前索取驗證碼。"), ("冒用帳號或身分", "朋友、主管、創作者或客服人員要求驗證碼、禮品卡、轉帳或機密資料。"), ("假技術支援", "彈出視窗聲稱裝置感染病毒，要求你打電話或開啟遠端控制；應改用官方支援管道。"), ("中獎或感情請求", "意外中獎、緊急旅費或培養感情最後變成要錢、保密或取得帳戶權限。")],
        "steps_heading": "通用的初步檢查順序", "steps": [("先暫停對方要求的動作", "在故事尚未查證前，不要點擊、付款、下載、轉帳、分享驗證碼或開放遠端存取。"), ("把訊息與主張分開", "標誌、來電顯示、帳號名稱和熟悉的語氣都可能被複製；請檢查真正的網址、帳戶與要求。"), ("離開訊息本身再確認", "自行輸入官方網站、開啟官方 App，或使用你原本知道的電話；不要使用訊息提供的聯絡方式。"), ("如果已經行動，先保護帳戶", "用可信任的裝置更改外洩密碼，聯絡銀行或服務商、回報訊息並保留證據。")],
        "safe": "安全輸入規則：使用 MindDividend Shield 時，只提供刪除個資後的例子。不要貼上密碼、付款資料、驗證碼、身分證件或私人地址。", "languages_heading": "選擇閱讀語言",
        "share_heading": "分享公開指南", "share": "請分享這份公開指南，不要轉傳含有私人資料的訊息。分享前移除密碼、驗證碼、付款資料和身分資訊。",
        "cta_heading": "不確定，就是放慢速度的理由。", "cta": "用不含敏感資料的例子做初步檢查，再透過官方管道確認。", "open": "開啟 MindDividend Shield",
        "home": "首頁", "checker_label": "訊息檢查器", "global": "全球檢查器", "report": "回報詐騙", "privacy": "安全與隱私", "directory": "全部安全指南",
    },
    "common-online-scams-id.html": {
        "lang": "id", "checker": "pemeriksa-pesan-penipuan.html", "campaign": "scams_id",
        "title": "Penipuan Online yang Umum: Panduan Pemeriksaan Awal",
        "description": "Kenali tanda bahaya penipuan bank, pengiriman, pekerjaan, investasi, marketplace, penyamaran akun, dan dukungan teknis palsu.",
        "hero1": "Cerita penipuan online berbeda.", "hero2": "Pola tekanannya sering sama.",
        "dek": "Panduan praktis ini membantu mengenali tanda bahaya pertama pada pesan bank, pengiriman, pekerjaan, investasi, marketplace, akun sosial, dan dukungan teknis palsu.",
        "check": "Periksa pesan mencurigakan", "scenarios": "Delapan skenario penipuan umum", "intro": "Merek dan ceritanya berubah menurut negara. Permintaannya sering mendorong Anda bertindak sebelum memeriksa.",
        "cards": [("Peringatan bank palsu", "Peringatan akun yang mendesak meminta Anda masuk lewat tautan, mengonfirmasi kode, atau memindahkan uang demi alasan keamanan."), ("Pemberitahuan pengiriman palsu", "Pesan mengaku ada masalah alamat atau biaya pengiriman kecil lalu mengarahkan Anda ke halaman pembayaran tiruan."), ("Tawaran kerja online", "Perekrut menjanjikan penghasilan mudah lalu meminta uang, setoran kripto, dokumen pribadi, atau pengiriman ulang paket."), ("Tawaran investasi atau kripto", "Keuntungan yang dijamin, grup rahasia, dukungan selebritas, dan tekanan untuk terus menyetor adalah tanda risiko."), ("Pembeli atau penjual marketplace", "Seseorang mendorong Anda keluar dari platform, mengirim bukti pembayaran palsu, membayar lebih, atau meminta kode verifikasi."), ("Penyamaran akun", "Teman, atasan, kreator, atau agen dukungan meminta kode, kartu hadiah, transfer, atau informasi rahasia."), ("Dukungan teknis palsu", "Peringatan pop-up mengaku perangkat terinfeksi lalu memberi nomor telepon atau meminta akses jarak jauh. Gunakan dukungan resmi."), ("Permintaan hadiah atau hubungan", "Hadiah tak terduga, masalah perjalanan mendesak, atau hubungan emosional berubah menjadi permintaan uang, rahasia, atau akses akun.")],
        "steps_heading": "Urutan pemeriksaan awal yang berlaku umum", "steps": [("Hentikan tindakan yang diminta", "Jangan mengeklik, membayar, mengunduh, mentransfer, membagikan kode, atau memberi akses jarak jauh sebelum ceritanya terverifikasi."), ("Pisahkan pesan dari klaimnya", "Logo, identitas penelepon, nama profil, dan gaya bahasa dapat disalin. Periksa alamat, akun, dan permintaan yang sebenarnya."), ("Verifikasi di luar pesan", "Ketik situs resmi sendiri, buka aplikasi resmi, atau hubungi nomor yang sudah dikenal. Jangan gunakan kontak dari pesan."), ("Lindungi akun jika sudah bertindak", "Ganti kata sandi dari perangkat tepercaya, hubungi bank atau penyedia layanan, laporkan pesan, dan simpan bukti.")],
        "safe": "Aturan input aman: gunakan contoh yang sudah menghapus data pribadi di MindDividend Shield. Jangan pernah menempelkan kata sandi, detail pembayaran, kode verifikasi, dokumen identitas, atau alamat pribadi.", "languages_heading": "Gunakan panduan dalam bahasa Anda",
        "share_heading": "Bagikan panduan publik", "share": "Bagikan panduan ini, bukan pesan pribadi. Hapus kata sandi, kode, detail pembayaran, dan identitas sebelum berbagi.",
        "cta_heading": "Keraguan adalah alasan untuk berhenti sejenak.", "cta": "Lakukan pemeriksaan awal dengan contoh tanpa data sensitif, lalu verifikasi melalui saluran resmi.", "open": "Buka MindDividend Shield",
        "home": "Beranda", "checker_label": "Pemeriksa pesan", "global": "Pemeriksaan global", "report": "Laporkan penipuan", "privacy": "Keamanan dan privasi", "directory": "Semua panduan keamanan",
    },
    "common-online-scams-vi.html": {
        "lang": "vi", "checker": "kiem-tra-tin-nhan-lua-dao.html", "campaign": "scams_vi",
        "title": "Các trò lừa đảo trực tuyến phổ biến: Hướng dẫn kiểm tra ban đầu",
        "description": "Nhận biết dấu hiệu lừa đảo ngân hàng, giao hàng, việc làm, đầu tư, sàn mua bán, giả mạo tài khoản và hỗ trợ kỹ thuật.",
        "hero1": "Câu chuyện lừa đảo trực tuyến thay đổi.", "hero2": "Cách gây áp lực thường giống nhau.",
        "dek": "Hướng dẫn thực tế giúp bạn nhận biết dấu hiệu cảnh báo sớm trong tin nhắn ngân hàng, giao hàng, việc làm, đầu tư, mua bán, tài khoản mạng xã hội và hỗ trợ kỹ thuật giả.",
        "check": "Kiểm tra tin nhắn đáng ngờ", "scenarios": "Tám tình huống lừa đảo phổ biến", "intro": "Thương hiệu và câu chuyện thay đổi theo từng nước. Yêu cầu thường nhằm khiến bạn hành động trước khi kiểm tra.",
        "cards": [("Cảnh báo ngân hàng giả", "Cảnh báo khẩn cấp yêu cầu đăng nhập qua liên kết, xác nhận mã hoặc chuyển tiền để giữ an toàn."), ("Thông báo giao hàng giả", "Tin nhắn nói địa chỉ có vấn đề hoặc cần trả một khoản phí nhỏ rồi đưa bạn đến trang thanh toán giả."), ("Lời mời việc làm trực tuyến", "Người tuyển dụng hứa hẹn thu nhập dễ dàng rồi yêu cầu tiền, tiền điện tử, giấy tờ hoặc chuyển tiếp hàng."), ("Lời mời đầu tư hoặc tiền số", "Lợi nhuận được bảo đảm, nhóm bí mật, người nổi tiếng quảng bá và áp lực nạp thêm đều là dấu hiệu rủi ro."), ("Người mua hoặc bán trên sàn", "Đối phương muốn đưa giao dịch ra ngoài nền tảng, gửi biên lai giả, trả thừa hoặc xin mã xác minh."), ("Mạo danh tài khoản", "Bạn bè, quản lý, nhà sáng tạo hoặc nhân viên hỗ trợ yêu cầu mã, thẻ quà tặng, chuyển khoản hoặc thông tin bí mật."), ("Hỗ trợ kỹ thuật giả", "Cửa sổ cảnh báo nói thiết bị nhiễm virus rồi đưa số điện thoại hoặc xin quyền điều khiển từ xa. Hãy dùng hỗ trợ chính thức."), ("Yêu cầu về giải thưởng hoặc tình cảm", "Giải thưởng bất ngờ, sự cố du lịch hoặc mối quan hệ tình cảm cuối cùng biến thành yêu cầu tiền, giữ bí mật hoặc truy cập tài khoản.")],
        "steps_heading": "Trình tự kiểm tra ban đầu", "steps": [("Tạm dừng hành động được yêu cầu", "Không nhấp, trả tiền, tải xuống, chuyển khoản, chia sẻ mã hoặc cho quyền truy cập từ xa khi câu chuyện chưa được xác minh."), ("Tách tin nhắn khỏi lời khẳng định", "Logo, tên người gọi, tên hồ sơ và giọng điệu quen thuộc có thể bị sao chép. Hãy kiểm tra địa chỉ, tài khoản và yêu cầu thật."), ("Xác minh bên ngoài tin nhắn", "Tự nhập trang web chính thức, mở ứng dụng chính thức hoặc gọi số đã biết. Không dùng thông tin liên hệ trong tin nhắn."), ("Bảo vệ tài khoản nếu đã hành động", "Đổi mật khẩu bằng thiết bị đáng tin cậy, liên hệ ngân hàng hoặc nhà cung cấp, báo cáo tin nhắn và giữ lại bằng chứng.")],
        "safe": "Quy tắc nhập an toàn: chỉ dùng ví dụ đã xóa thông tin riêng tư với MindDividend Shield. Không dán mật khẩu, thông tin thanh toán, mã xác minh, giấy tờ tùy thân hoặc địa chỉ riêng.", "languages_heading": "Đọc hướng dẫn bằng ngôn ngữ của bạn",
        "share_heading": "Chia sẻ hướng dẫn công khai", "share": "Hãy chia sẻ hướng dẫn công khai thay vì chuyển tiếp tin nhắn riêng. Xóa mật khẩu, mã, thông tin thanh toán và danh tính trước khi chia sẻ.",
        "cta_heading": "Không chắc chắn là lý do để chậm lại.", "cta": "Kiểm tra ban đầu bằng ví dụ không có dữ liệu nhạy cảm, sau đó xác minh qua kênh chính thức.", "open": "Mở MindDividend Shield",
        "home": "Trang chủ", "checker_label": "Kiểm tra tin nhắn", "global": "Kiểm tra toàn cầu", "report": "Báo cáo lừa đảo", "privacy": "An toàn và quyền riêng tư", "directory": "Tất cả hướng dẫn an toàn",
    },
    "common-online-scams-ja.html": {
        "lang": "ja", "checker": "scam-message-checker-ja.html", "campaign": "scams_ja",
        "title": "よくあるネット詐欺：最初に確認するための実用ガイド",
        "description": "偽の銀行通知、配送、求人、投資、マーケットプレイス、アカウントなりすまし、偽サポートの危険サインを確認します。",
        "hero1": "ネット詐欺の話は変わります。", "hero2": "急がせるパターンは同じです。",
        "dek": "銀行通知、配送、求人、投資、フリマ、SNSアカウント、偽のテクニカルサポートにある初期サインを、クリックや支払いの前に確認するガイドです。",
        "check": "不審なメッセージを確認", "scenarios": "よくある8つの詐欺パターン", "intro": "ブランドや話の内容は国によって変わりますが、確認する前に行動させようとする点は共通しています。",
        "cards": [("偽の銀行アラート", "緊急の口座警告でリンクからのログイン、コードの確認、安全のための送金を求めます。"), ("偽の配送通知", "住所の問題や少額の再配達料を理由に、偽の決済ページへ誘導します。"), ("オンライン求人", "簡単な収入を約束した後、費用、暗号資産、身分証、商品の転送を求めます。"), ("投資・暗号資産の勧誘", "利益保証、秘密のグループ、有名人の推薦、追加入金への圧力は危険サインです。"), ("フリマの買い手・売り手", "プラットフォーム外への移動、偽の入金画面、過払い、認証コードを求めることがあります。"), ("アカウントのなりすまし", "友人、上司、クリエイター、サポート担当を装い、コードや送金、秘密情報を求めます。"), ("偽のテクニカルサポート", "感染を知らせるポップアップから電話や遠隔操作を求めます。公式サポートを利用してください。"), ("当選・恋愛を利用した要求", "突然の当選、旅行のトラブル、親密さが金銭や秘密、アカウント権限の要求に変わります。")],
        "steps_heading": "共通する最初の確認手順", "steps": [("求められた操作を止める", "確認できるまでクリック、支払い、ダウンロード、送金、コード共有、遠隔アクセスをしないでください。"), ("メッセージと主張を分ける", "ロゴ、発信者番号、プロフィール名、口調はコピーできます。本当のURL、アカウント、要求を確認します。"), ("メッセージの外で確認する", "公式サイトを自分で入力し、公式アプリを開くか、知っている番号に連絡してください。メッセージ内の連絡先は使いません。"), ("操作した場合はアカウントを守る", "信頼できる端末でパスワードを変更し、銀行やサービスに連絡し、報告して証拠を保存します。")],
        "safe": "安全な入力ルール：MindDividend Shieldには個人情報を削除した例だけを入力してください。パスワード、決済情報、認証コード、本人確認書類、住所は入力しないでください。", "languages_heading": "自分の言語でガイドを読む",
        "share_heading": "公開ガイドを共有する", "share": "個人的なメッセージを転送する代わりに、この公開ガイドを共有してください。共有前にパスワード、コード、支払い情報、個人情報を削除します。",
        "cta_heading": "迷ったら、いったん立ち止まる理由です。", "cta": "機密情報のない例で最初の確認を行い、その後は公式窓口で確認してください。", "open": "MindDividend Shieldを開く",
        "home": "ホーム", "checker_label": "メッセージチェッカー", "global": "グローバルチェッカー", "report": "詐欺を報告", "privacy": "安全とプライバシー", "directory": "安全ガイド一覧",
    },
    "common-online-scams-ko.html": {
        "lang": "ko", "checker": "scam-message-checker-ko.html", "campaign": "scams_ko",
        "title": "흔한 온라인 사기: 안전한 첫 확인 가이드",
        "description": "가짜 은행 알림, 배송, 일자리, 투자, 거래 플랫폼, 계정 사칭, 가짜 기술 지원의 위험 신호를 확인하세요.",
        "hero1": "온라인 사기의 이야기는 달라집니다.", "hero2": "압박하는 방식은 대체로 같습니다.",
        "dek": "은행 알림, 배송, 일자리, 투자, 거래 플랫폼, 소셜 계정, 가짜 기술 지원에서 클릭·결제·답장 전에 초기 위험 신호를 확인하는 실용 가이드입니다.",
        "check": "의심스러운 메시지 확인", "scenarios": "흔한 사기 시나리오 8가지", "intro": "브랜드와 이야기는 나라에 따라 달라집니다. 하지만 확인하기 전에 행동하게 만드는 요구는 비슷합니다.",
        "cards": [("가짜 은행 알림", "긴급한 계정 경고로 링크 로그인, 인증 코드 확인 또는 안전을 이유로 송금을 요구합니다."), ("가짜 배송 알림", "주소 문제나 소액 재배송 비용을 핑계로 가짜 결제 페이지로 보냅니다."), ("온라인 일자리 제안", "쉬운 수입을 약속한 뒤 돈, 암호화폐, 신분증 또는 물품 재배송을 요구합니다."), ("투자·암호화폐 권유", "수익 보장, 비밀 그룹, 유명인 추천, 추가 입금 압박은 위험 신호입니다."), ("거래 플랫폼 구매자·판매자", "플랫폼 밖으로 이동시키거나 가짜 결제 증명, 초과 지불, 인증 코드를 요구합니다."), ("계정 사칭", "친구, 관리자, 크리에이터 또는 지원 담당자를 사칭해 코드, 상품권, 송금, 비밀 정보를 요청합니다."), ("가짜 기술 지원", "기기에 바이러스가 있다고 알리고 전화나 원격 접근을 요구합니다. 공식 지원을 이용하세요."), ("당첨·연애를 이용한 요청", "뜻밖의 당첨, 긴급한 여행 문제, 감정적 관계가 돈·비밀·계정 접근 요청으로 바뀝니다.")],
        "steps_heading": "공통되는 첫 확인 순서", "steps": [("요청받은 행동을 멈추기", "확인하기 전에는 클릭, 결제, 다운로드, 송금, 코드 공유, 원격 접근을 하지 마세요."), ("메시지와 주장을 나누어 보기", "로고, 발신자 표시, 프로필 이름, 익숙한 말투는 복제될 수 있습니다. 실제 주소·계정·요청을 확인하세요."), ("메시지 밖에서 확인하기", "공식 웹사이트를 직접 입력하고 공식 앱을 열거나 알고 있는 번호로 연락하세요. 메시지 속 연락처는 사용하지 마세요."), ("행동했다면 계정 보호하기", "신뢰할 수 있는 기기에서 비밀번호를 바꾸고 은행이나 서비스 제공자에게 연락해 신고하고 증거를 보관하세요.")],
        "safe": "안전한 입력 규칙: MindDividend Shield에는 개인정보를 지운 예시만 넣으세요. 비밀번호, 결제 정보, 인증 코드, 신분증, 개인 주소는 절대 입력하지 마세요.", "languages_heading": "원하는 언어로 가이드 보기",
        "share_heading": "공개 가이드 공유하기", "share": "개인 메시지를 전달하는 대신 이 공개 가이드를 공유하세요. 공유 전에 비밀번호, 코드, 결제 정보와 신원을 지우세요.",
        "cta_heading": "확실하지 않다면 잠시 멈출 이유입니다.", "cta": "민감한 정보가 없는 예시로 먼저 확인한 다음 공식 채널에서 검증하세요.", "open": "MindDividend Shield 열기",
        "home": "홈", "checker_label": "메시지 검사기", "global": "글로벌 검사기", "report": "사기 신고", "privacy": "안전 및 개인정보 보호", "directory": "모든 안전 가이드",
    },
    "common-online-scams-it.html": {
        "lang": "it", "checker": "controllo-messaggio-truffa.html", "campaign": "scams_it",
        "title": "Truffe online comuni: guida pratica al primo controllo",
        "description": "Riconosci i segnali di truffe bancarie, consegne, lavoro, investimenti, marketplace, impersonificazione e falso supporto tecnico.",
        "hero1": "Le storie delle truffe online cambiano.", "hero2": "Lo schema della pressione spesso è lo stesso.",
        "dek": "Una guida pratica per riconoscere i primi segnali nei messaggi bancari, nelle consegne, nelle offerte di lavoro, negli investimenti, nei marketplace e nel falso supporto tecnico.",
        "check": "Controlla un messaggio sospetto", "scenarios": "Otto scenari di truffa comuni", "intro": "Il marchio e la storia cambiano da paese a paese. La richiesta cerca spesso di farti agire prima di verificare.",
        "cards": [("Falso avviso bancario", "Un avviso urgente chiede di accedere tramite un link, confermare un codice o spostare denaro per sicurezza."), ("Falsa notifica di consegna", "Un messaggio segnala un problema con l'indirizzo o una piccola spesa e porta a una pagina di pagamento imitata."), ("Offerta di lavoro online", "Un presunto recruiter promette guadagni facili e poi chiede denaro, criptovalute, documenti o di inoltrare pacchi."), ("Proposta di investimento o crypto", "Rendimenti garantiti, gruppi segreti, celebrità e pressione per versare altro denaro sono segnali di rischio."), ("Acquirente o venditore sul marketplace", "La persona vuole uscire dalla piattaforma, manda una ricevuta falsa, paga troppo o chiede un codice di verifica."), ("Impersonificazione di un account", "Un amico, manager, creator o operatore di supporto chiede codici, gift card, bonifici o informazioni riservate."), ("Falso supporto tecnico", "Un pop-up dice che il dispositivo è infetto e chiede un numero o l'accesso remoto. Usa il supporto ufficiale."), ("Premio o richiesta romantica", "Un premio inatteso, un problema di viaggio o una relazione diventano una richiesta di denaro, segretezza o accesso all'account.")],
        "steps_heading": "La sequenza universale del primo controllo", "steps": [("Fermati prima dell'azione richiesta", "Non cliccare, pagare, scaricare, trasferire, condividere codici o concedere accesso remoto finché la storia non è verificata."), ("Separa il messaggio dalla sua pretesa", "Logo, numero chiamante, nome del profilo e tono possono essere copiati. Controlla indirizzo, account e richiesta reali."), ("Verifica fuori dal messaggio", "Digita tu il sito ufficiale, apri l'app ufficiale o chiama un numero già conosciuto. Non usare i contatti del messaggio."), ("Proteggi l'account se hai agito", "Cambia le password da un dispositivo affidabile, contatta banca o fornitore, segnala il messaggio e conserva le prove.")],
        "safe": "Regola per l'input sicuro: usa con MindDividend Shield solo un esempio senza dati personali. Non incollare password, dati di pagamento, codici, documenti o indirizzi privati.", "languages_heading": "Usa la guida nella tua lingua",
        "share_heading": "Condividi la guida pubblica", "share": "Condividi questa guida invece di inoltrare un messaggio privato. Rimuovi password, codici, pagamenti e dati personali prima di condividere.",
        "cta_heading": "L'incertezza è un motivo per rallentare.", "cta": "Fai un primo controllo con un esempio non sensibile, poi verifica attraverso il canale ufficiale.", "open": "Apri MindDividend Shield",
        "home": "Home", "checker_label": "Controllo messaggi", "global": "Controllo globale", "report": "Segnala una truffa", "privacy": "Sicurezza e privacy", "directory": "Tutte le guide di sicurezza",
    },
}


def link_list(separator=" · "):
    return separator.join(f'<a class="link" href="{file}">{escape(label)}</a>' for label, file in LANGUAGE_LINKS)


def render(filename, d, stamp):
    url = BASE + filename
    alt_lines = "\n".join(f'<link rel="alternate" hreflang="{lang}" href="{BASE}{file}">' for lang, file in ALTERNATES)
    cards = "".join(f'<article class="card"><h3>{escape(title)}</h3><p>{escape(text)}</p></article>' for title, text in d["cards"])
    steps = "".join(f'<div class="step"><div><h3>{escape(title)}</h3><p class="muted">{escape(text)}</p></div></div>' for title, text in d["steps"])
    article_json = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": d["title"], "description": d["description"], "url": url,
        "datePublished": "2026-08-18T00:00:00+08:00", "dateModified": stamp,
        "author": {"@type": "Organization", "name": "Alpha Engineer", "url": BASE},
        "publisher": {"@type": "Organization", "name": "Alpha Engineer", "url": BASE},
        "image": BASE + "og-shield.png", "inLanguage": d["lang"],
    }, ensure_ascii=False, separators=(",", ":"))
    breadcrumb_json = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": d["title"], "item": url},
        ],
    }, ensure_ascii=False, separators=(",", ":"))
    campaign = escape(d["campaign"])
    tool_url = f'{SHIELD}?utm_source=alphaengineerai&amp;utm_medium=seo&amp;utm_campaign={campaign}'
    share_url = f'{url}?utm_source=site&amp;utm_medium=share&amp;utm_campaign={campaign}'
    share_encoded = share_url.replace("&amp;", "%26").replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("=", "%3D")
    return f'''<!DOCTYPE html>
<html lang="{escape(d["lang"])}">
<head>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(d["title"])}</title>
<meta name="description" content="{escape(d["description"])}">
<link rel="canonical" href="{url}">
{alt_lines}
<link rel="alternate" hreflang="x-default" href="{BASE}common-online-scams.html">
<link rel="stylesheet" href="minddividend-guides.css">
<meta property="og:title" content="{escape(d["title"])} | MindDividend Shield">
<meta property="og:description" content="{escape(d["description"])}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}og-shield.png">
<meta property="og:site_name" content="MindDividend Shield">
<meta property="og:image:alt" content="MindDividend Shield — a free first check for suspicious messages">
<script type="application/ld+json">
{article_json}
</script>
<script src="/analytics.js" defer></script>
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(d["title"])} | MindDividend Shield">
<meta name="twitter:description" content="{escape(d["description"])}">
<meta name="twitter:url" content="{url}">
<meta name="twitter:image" content="{BASE}og-shield.png">
<script type="application/ld+json">{breadcrumb_json}</script>
<link rel="alternate" type="application/rss+xml" title="MindDividend Shield Safety Guides" href="{BASE}feed.xml">
</head>
<body>
<header class="container"><a class="logo" href="/">Alpha <span>Engineer</span></a><nav><a href="minddividend-shield.html">Shield</a><a href="{d["checker"]}">{escape(d["checker_label"])}</a></nav></header>
<main>
<section class="hero container"><div class="eyebrow">MindDividend Shield · {escape(d["lang"])}</div><h1>{escape(d["hero1"])} <span>{escape(d["hero2"])}</span></h1><p class="dek">{escape(d["dek"])}</p><a class="btn" href="{tool_url}" target="_blank" rel="noopener" data-analytics-event="checker_open" data-analytics-target="shield_tool">{escape(d["check"])}</a></section>
<section><div class="container"><h2>{escape(d["scenarios"])}</h2><p class="muted">{escape(d["intro"])}</p><div class="grid">{cards}</div></div></section>
<section><div class="container"><h2>{escape(d["steps_heading"])}</h2><div class="steps">{steps}</div><div class="callout"><strong>{escape(d["safe"])}</strong></div></div></section>
<section><div class="container"><h2>{escape(d["languages_heading"])}</h2><p class="muted">{link_list()}</p></div></section>
<section><div class="container"><h2>{escape(d["share_heading"])}</h2><p class="muted">{escape(d["share"])}</p><div class="share-strip"><a class="share-link" href="https://x.com/intent/post?text=Pause%20before%20you%20click%20or%20pay.&amp;url={share_encoded}" target="_blank" rel="noopener" data-analytics-event="guide_share_click" data-analytics-target="x">X</a><a class="share-link" href="https://www.facebook.com/sharer/sharer.php?u={share_encoded}" target="_blank" rel="noopener" data-analytics-event="guide_share_click" data-analytics-target="facebook">Facebook</a><a class="share-link" href="https://www.linkedin.com/sharing/share-offsite/?url={share_encoded}" target="_blank" rel="noopener" data-analytics-event="guide_share_click" data-analytics-target="linkedin">LinkedIn</a><a class="share-link" href="https://wa.me/?text=Pause%20before%20you%20click%20or%20pay%3A%20{share_encoded}" target="_blank" rel="noopener" data-analytics-event="guide_share_click" data-analytics-target="whatsapp">WhatsApp</a></div></div></section>
<section class="cta"><div class="container"><h2>{escape(d["cta_heading"])}</h2><p class="muted">{escape(d["cta"])}</p><a class="btn" href="{tool_url}" target="_blank" rel="noopener" data-analytics-event="checker_open" data-analytics-target="shield_tool">{escape(d["open"])} &rarr;</a></div></section>
</main>
<footer class="container"><div>&copy; 2026 Alpha Engineer</div><div class="links"><a class="link" href="/">{escape(d["home"])}</a><a class="link" href="{d["checker"]}">{escape(d["checker_label"])}</a><a class="link" href="global-online-scam-checker.html">{escape(d["global"])}</a><a class="link" href="report-online-scam.html">{escape(d["report"])}</a><a class="link" href="privacy-and-safety.html">{escape(d["privacy"])}</a><a class="link" href="guide-directory.html">{escape(d["directory"])}</a></div></footer>
</body>
</html>
'''


for filename, data in PAGES.items():
    path = ROOT / filename
    stamp = STAMP
    if path.exists():
        previous = re.search(r'"dateModified":"([^"]+)"', path.read_text(encoding="utf-8"))
        if previous:
            stamp = previous.group(1)
    path.write_text(render(filename, data, stamp), encoding="utf-8", newline="")
    print(f"WROTE {filename}")
