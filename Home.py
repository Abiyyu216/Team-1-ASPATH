import streamlit as st

st.set_page_config(page_title="TEAM 1 ASPATH", layout="centered", page_icon="😎")

st.markdown(
    """
    <style>
    /* 1. Ubah warna latar belakang header Streamlit */
    [data-testid="stHeader"] {
        background-color:rgb(53, 122, 192); /* Navy */
    }
    
    /* Ubah background utama aplikasi menjadi navy blue */
    .stApp {
        background-color:rgb(53, 122, 192);
    }
    
    /* Ubah background sidebar menjadi navy blue */
    [data-testid="stSidebar"] {
        background-color:rgb(12, 67, 122);
    }
    
    /* Warna teks untuk halaman utama (seluruh area aplikasi kecuali sidebar) */
    .stApp * {
        color:rgb(255, 255, 255);
    }
    
    /* Warna teks untuk sidebar */
    [data-testid="stSidebar"] * {
        color:rgb(255, 255, 255) !important;
    }
    
    /* Styling untuk tombol agar serasi dengan tema */
    div.stButton > button {
        background-color: rgb(13, 61, 109);
        color: #ffffff;
        border: 1px solid #ffffff;
    }

    /* Efek hover ketika cursor berada di atas tombol */
    .stButton > button:first-child:hover {
        background-color:rgb(28, 111, 195); /* Warna lebih terang saat hover */
        border: 2px solid #004080;
        }

    /* Efek saat tombol ditekan */
    .stButton > button:first-child:active {
        background-color: #003366; /* Warna lebih gelap saat ditekan */
        border: 2px solid #002244;
        }
    
    /* Styling untuk search bar input field */
    div[data-testid="stTextInput"] input {
        background-color:rgb(43, 108, 172); /* Navy blue background */
        color: #ffffff;           /* White text */
        border: 1px solid #ffffff;
        padding: 0.5rem;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

st.subheader("Belajar apa kita hari ini?")
st.markdown(
    """
    <style>
    div[data-testid="stTextInput"] { margin-top: -50px; }
    div[data-testid="stTextInput"]::after {
        content: "🔍";
        position: absolute;
        right: 10px;
        top: 70%;
        transform: translateY(-50%);
        font-size: 1.2rem;
        pointer-events: none; /* Agar emoji tidak mengganggu interaksi pada input */
    }
    </style>
    """, unsafe_allow_html=True
    )
search_query = st.text_input("", key="homepage_search")
    
# Dictionary yang berisi judul materi beserta ringkasan isi materi (digunakan untuk pencarian full-text)
materials = {
    "Daftar Anggota Kelompok": "Daftar anggota kelompok: Abiyyu Daffa Adzkiya, Fatimah Nurul Hidayah, Jethro Eureka Sinaga, Muhammad Rahel Al Islami, Nathania Fernanda Soti Simbolon, Satria Adinata Pria Ardana.",
    "Pengertian dan Manfaat Jaringan": "Jaringan komputer adalah kumpulan beberapa komputer dan perangkat lainnya yang saling terhubung satu sama lainnya melalui media perantara. Manfaat: resource sharing, reliabilitas tinggi, kemudahan akses informasi, dan media hiburan.",
    "Jenis-Jenis Jaringan Komputer": "Berdasarkan area skala: Local Area Network (LAN), Wide Area Network (WAN), Internet. Berdasarkan media penghantar: Wire Network, Wireless Network. Berdasarkan fungsi: client server, peer to peer. Berdasarkan topologi: star, bus, ring.",
    "Keamanan dan Ancaman Jaringan": "Keamanan jaringan. Prinsip keamanan jaringan: confidentiality, integrity, availability, authentication, nonrepudiation. Ancaman jaringan. Gangguan jaringan berdasarkan sumbernya: external attack, internal attack. Kategori gangguan: interruption, interception, modification, fabrication.",
    "Latihan Soal": "Kuis pilihan ganda.",
    "Dokumentasi Kelompok": "Dokumentasi kelompok."
    }
    
if search_query:
    # Lakukan pencarian pada judul dan isi materi
    results = []
    for title, content in materials.items():
        if search_query.lower() in title.lower() or search_query.lower() in content.lower():
            results.append(title)
    if results:
        for result in results:
            if st.button(result, key="search_result_" + result):
                st.session_state.page = result
                st.rerun()
    else:
        st.write("Tidak ditemukan hasil.")

def show_anggota():
    st.markdown("---")

    members = [
        {"nama": "Abiyyu Daffa Adzkiya", "nim": "4131240255", "gambar": r"C:\Users\Asus\Downloads\Abiyyu_1.jpg"},
        {"nama": "Fatimah Nurul Hidayah", "nim": "4131240291", "gambar": r"C:\Users\Asus\Downloads\Fatimah.jpg"},
        {"nama": "Jethro Eureka Sinaga", "nim": "4131240294", "gambar": r"C:\Users\Asus\Downloads\Jethro.jpg"},
        {"nama": "Muhammad Rahel Al Islami", "nim": "4131240397", "gambar": r"C:\Users\Asus\Downloads\Rahel.jpg"},
        {"nama": "Nathania Fernanda Soti Simbolon", "nim": "4131240322", "gambar": r"C:\Users\Asus\Downloads\Nathan.jpg"},
        {"nama": "Satria Adinata Pria Ardana", "nim": "4131240341", "gambar": r"C:\Users\Asus\Downloads\Satria.jpg"},
    ]

    cols = st.columns(3)

    for i, member in enumerate(members):
        with cols[i % 3]:
            st.image(member["gambar"], width=200)
            st.markdown(f"**{member['nama']}**")
            st.markdown(f"📌 NIM: {member['nim']}")
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")


def show_pengertian():
    st.subheader("Pengertian Jaringan")
    st.write("Jaringan komputer adalah kumpulan beberapa komputer dan perangkat lainnya yang saling terhubung satu sama lainnya melalui media perantara.")
    st.write("")
    st.subheader("Manfaat Jaringan")
    st.write("- Resource sharing\n"
             "- Reliabilitas tinggi untuk menyimpan data di tempat lain\n"
             "- Kemudahan akses informasi\n"
             "- Dapat menjadi media hiburan")
    st.image(r"C:\Users\Asus\Downloads\Gambar 1.png")
    st.write("")
    st.write("")
    st.subheader("Perkembangan Internet")
    st.video("https://youtu.be/FAXt3cdcz6s?si=DyFk0E0wDQAB6vnX")
    st.write("")
    st.image(r"C:\Users\Asus\Downloads\Gambar 2.png", width=700, caption="Perangkat elektronik yang sudah terdapat wifi di dalamnya")


def show_jenis():
    st.subheader("Berdasarkan Area atau Skala")
    st.markdown("**Local Area Network (LAN)**")
    st.write("Jaringan dalam lingkungan terbatas seperti kantor, sekolah, atau rumah.")
    st.write("Contoh: Jaringan komputer di sebuah perusahaan yang menghubungkan komputer, printer, dan server dalam satu gedung.")
    st.markdown("**Wide Area Network (WAN)**")
    st.write("Jaringan yang mencakup area geografis luas, sering kali menghubungkan beberapa LAN.")
    st.write("Contoh: Jaringan antar cabang bank di berbagai kota yang saling terhubung melalui jaringan telekomunikasi.")
    st.markdown("**Internet**")
    st.write("Jaringan global yang menghubungkan miliaran perangkat di seluruh dunia.")
    st.write("Contoh: Akses ke website, email, dan layanan cloud melalui koneksi internet.")
    st.write("")

    st.subheader("Berdasarkan Media Penghantar")
    st.markdown("**Wire Network**")
    st.write("Kelebihan:")
    st.write("- Stabil dan memiliki kecepatan tinggi.\n"
             "- Lebih aman karena sulit disadap dari luar.\n"
             "- Minim gangguan dari faktor lingkungan.")
    st.write("Kekurangan:")
    st.write("- Kurang fleksibel karena membutuhkan kabel fisik.\n"
             "- Instalasi dan pemeliharaan lebih kompleks dan mahal.")
    st.markdown("**Wireless Network**")
    st.write("Kelebihan:")
    st.write("- Fleksibel dan mudah digunakan tanpa perlu kabel.\n"
             "- Mudah diperluas dan diakses dari berbagai lokasi.\n"
             "- Biaya pemasangan lebih rendah dibandingkan jaringan kabel.")
    st.write("Kekurangan:")
    st.write("- Kecepatan dan stabilitas lebih rendah dibanding jaringan kabel.\n"
             "- Lebih rentan terhadap gangguan sinyal dan penyadapan.")
    st.write("")

    st.subheader("Berdasarkan Fungsi")
    st.markdown("**Client Server**")
    st.write("Jaringan dengan server sebagai pusat layanan, sementara client mengaksesnya.")
    st.write("Contoh: Jaringan bank yang mengelola data nasabah melalui server pusat.")
    st.markdown("**Peer to Peer**")
    st.write("Jaringan di mana setiap komputer bisa berbagi data tanpa server pusat.")
    st.write("Contoh: Jaringan antar komputer di rumah untuk berbagi file langsung.")
    st.write("")

    st.subheader("Berdasarkan Topologi")
    st.markdown("**Star**")
    st.image(r"C:\Users\Asus\Downloads\Gambar 3.png")
    st.markdown("**Bus**")
    st.image(r"C:\Users\Asus\Downloads\Gambar 4.png")
    st.markdown("**Ring**")
    st.image(r"C:\Users\Asus\Downloads\Picture5.png")


def show_keamanan():
    st.subheader("Keamanan Jaringan")
    st.write("Keamanan Jaringan adalah bentuk pencegahan atau deteksi gangguan pada sistem jaringan komputer dan sebagai perlindungan informasi terhadap pencurian data dan akses data oleh user yang tidak berhak.")
    st.write("")
    st.markdown("**Prinsip Keamanan Jaringan**")
    st.write("1. Confidentiality: informasi (data) hanya bida diakses oleh pihak yang memiliki hak.\n"
             "2. Integrity: informasi hanya dapat diubah oleh pihak yang memiliki hak.\n"
             "3. Availability: informasi tersedia untuk pihak yang memiliki hak ketika dibutuhkan.\n"
             "4. Authentication: pengirim informasi dapat diidentifikasi dengan benar dan ada jaminan identitas yang didapat tidak palsu.\n"
             "5. Nonrepudiation: pengirim maupun penerima informasi tidak dapat menyangkal pengiriman dan penerimaan pesan."
             )
    st.write("")
    st.subheader("Ancaman Jaringan")
    st.markdown("**Gangguan jaringan berdasarkan sumbernya**")
    st.write("1. External Attack")
    st.image(r"C:\Users\Asus\Downloads\Picture6.png")
    st.write("2. Internal Attack")
    st.image(r"C:\Users\Asus\Downloads\Picture7.png")
    st.write("")
    st.markdown("**Kategori Gangguan**")
    st.write("1. Interruption: suatu aset dari suatu sistem diserang sehingga menjadi tidak tersedia atau tidak dapat dipakai oleh pihak yang berwenang.\n"
             "2. Interception: suatu pihak (orang, program, atau sistem lain) yang tidak berwenang mendapatkan akses pada suatu aset.\n"
             "3. Modification: pihak yang tidak berwenang dapat melakukan perubahan terhadap suatu aset.\n"
             "4. Fabrication: pihak yang tidak berwenang menyisipkan objek palsu ke dalam sistem.\n")


def show_latihan():
    st.subheader("Kuis Pilihan Ganda")
    
    # Daftar pertanyaan, opsi, dan jawaban yang benar
    questions = [
        {
            "question": "Apa yang dimaksud dengan jaringan komputer?",
            "options": [
                "Sistem operasi untuk perangkat elektronik",
                "Kumpulan beberapa komputer dan perangkat lainnya yang saling terhubung melalui media perantara",
                "Perangkat keras yang digunakan untuk mengakses internet",
                "Protokol keamanan dalam sistem komputer"
            ],
            "answer": "Kumpulan beberapa komputer dan perangkat lainnya yang saling terhubung melalui media perantara"
        },
        {
            "question": "Manakah yang bukan merupakan manfaat dari jaringan komputer?",
            "options": [
                "Resource sharing",
                "Kemudahan akses informasi",
                "Menambah kapasitas penyimpanan perangkat",
                "Media hiburan"
            ],
            "answer": "Menambah kapasitas penyimpanan perangkat"
        },
        {
            "question": "Jenis jaringan komputer yang mencakup area geografis luas dan sering menghubungkan beberapa LAN disebut?",
            "options": [
                "Local Area Network (LAN)",
                "Wide Area Network (WAN)",
                "Peer to Peer Network",
                "Personal Area Network (PAN)"
            ],
            "answer": "Wide Area Network (WAN)"
        },
        {
            "question": "Apa kelebihan utama dari jaringan kabel (Wire Network)?",
            "options": [
                "Lebih fleksibel dibandingkan jaringan nirkabel",
                "Stabil dan memiliki kecepatan tinggi",
                "Mudah dipasang tanpa perlu banyak konfigurasi",
                "Tidak membutuhkan biaya instalasi"
            ],
            "answer": "Stabil dan memiliki kecepatan tinggi"
        },
        {
            "question": "Ancaman jaringan yang terjadi ketika pihak tidak berwenang mendapatkan akses pada suatu aset disebut?",
            "options": [
                "Interruption",
                "Interception",
                "Modification",
                "Fabrication"
            ],
            "answer": "Interception"
        },
        {
            "question": "Contoh penerapan jaringan Local Area Network (LAN) yang tepat adalah?",
            "options": [
                "Koneksi antar cabang bank di berbagai kota",
                "Jaringan komputer di dalam satu gedung perkantoran",
                "Sistem komunikasi satelit antar negara",
                "Akses internet di seluruh dunia"
            ],
            "answer": "Jaringan komputer di dalam satu gedung perkantoran"
        },
        {
            "question": "Jaringan yang menggunakan server sebagai pusat layanan dan client untuk mengakses data disebut?",
            "options": [
                "Peer to Peer",
                "Client Server",
                "Mesh Network",
                "Hybrid Network"
            ],
            "answer": "Client Server"
        },
        {
            "question": "Berikut ini merupakan kelemahan dari jaringan wireless, kecuali?",
            "options": [
                "Rentan terhadap gangguan sinyal",
                "Mudah disadap oleh pihak luar",
                "Biaya pemasangan lebih mahal dibandingkan jaringan kabel",
                "Kecepatan dan stabilitas lebih rendah dibandingkan jaringan kabel"
            ],
            "answer": "Biaya pemasangan lebih mahal dibandingkan jaringan kabel"
        },
        {
            "question": "Prinsip keamanan jaringan yang memastikan informasi hanya dapat diakses oleh pihak yang memiliki hak disebut?",
            "options": [
                "Integrity",
                "Authentication",
                "Confidentiality",
                "Availability"
            ],
            "answer": "Confidentiality"
        },
        {
            "question": "Jenis serangan jaringan yang terjadi ketika pihak yang tidak berwenang menyisipkan objek palsu ke dalam sistem disebut?",
            "options": [
                "Interception",
                "Modification",
                "Interruption",
                "Fabrication"
            ],
            "answer": "Fabrication"
        }
    ]
    
    # Menyimpan jawaban pengguna
    user_answers = {}
    
    # Menampilkan setiap pertanyaan dan opsi jawaban
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}.** {q['question']}")
        user_answers[i] = st.radio("Pilih jawaban:", q["options"], key=f"question_{i}", index=None)
    
    # Tombol submit untuk mengevaluasi jawaban
    if st.button("Submit Jawaban"):
        score = 0
        st.markdown("### Hasil Kuis")
        # Evaluasi jawaban pengguna dan tampilkan feedback untuk masing-masing pertanyaan
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                score += 1
                st.success(f"{i+1}. Benar!")
            else:
                st.error(f"{i+1}. Salah!")
                st.write(f"Jawaban Anda: **{user_answers[i]}**")
                st.write(f"Jawaban yang benar: **{q['answer']}**")
        st.markdown(f"**Skor Anda: {score} dari {len(questions)}**")
    
    st.markdown(
        """
        <style>
        .quiz-result-correct {
            background-color:rgb(135, 235, 158);
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .quiz-result-incorrect {
            background-color:rgb(251, 151, 159);
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
        )

    _original_success = st.success
    _original_error = st.error

    def custom_success(message, *args, **kwargs):
        st.markdown(f"<div class='quiz-result-correct'>{message}</div>", unsafe_allow_html=True)

    def custom_error(message, *args, **kwargs):
        st.markdown(f"<div class='quiz-result-incorrect'>{message}</div>", unsafe_allow_html=True)

    st.success = custom_success
    st.error = custom_error

    if st.button("Restart Kuis"):
        # Hapus kunci widget dari session state agar widget dibuat ulang pada pemuatan ulang halaman
        for i in range(len(questions)):
            if f"question_{i}" in st.session_state:
                del st.session_state[f"question_{i}"]


def show_dokumentasi():
    st.divider()
    st.subheader("Foto Kelompok")
    st.image(r"C:\Users\Asus\Downloads\Dokum.jpg")
    st.image(r"C:\Users\Asus\Downloads\Dokumen.jpg")
    st.image(r"C:\Users\Asus\Downloads\Dokumentasi.jpg")
    st.divider()
    st.subheader("JJ Dulu Gak Sieh😜🤙")
    st.video(r"C:\Users\Asus\Downloads\JJ1.mp4")


with st.sidebar:
    st.title("ASPATH🏆")
    st.image(r"C:\Users\Asus\Downloads\ASPATH PNG.png", width=150)
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    st.header("Jaringan & Telekomunikasi")
    
    with st.expander("🧑 ANGGOTA KELOMPOK"):
        if st.button("Lihat Anggota Kelompok"):
            st.session_state.page = "Daftar Anggota Kelompok"
            st.rerun()
    with st.expander("📂 MATERI"):
        if st.button("Pengertian & Manfaat"):
            st.session_state.page = "Pengertian dan Manfaat Jaringan"
            st.rerun()
        if st.button("Jenis-Jenis"):
            st.session_state.page = "Jenis-Jenis Jaringan Komputer"
            st.rerun()
        if st.button("Keamanan & Ancaman"):
            st.session_state.page = "Keamanan dan Ancaman Jaringan"
            st.rerun()
        if st.button("Latihan Soal"):
            st.session_state.page = "Latihan Soal"
            st.rerun()
    with st.expander("📷 DOKUMENTASI"):
        if st.button("Dokumentasi"):
            st.session_state.page = "Dokumentasi Kegiatan"
            st.rerun()

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.title("Welcome back to ASPATH! 🚀")
    st.write("Belajar jadi mudah bersama Team 1 ASPATH")
    st.image(r"C:\Users\Asus\Downloads\Purple Computer Class Google Classroom Header.png", width=750)
    st.write("")
    st.write("")

    # Contoh: Slider untuk mengukur tingkat minat
    interest = st.slider("Seberapa besar minat Anda untuk mempelajari materi Jaringan dan Telekomunikasi?", 0, 100, 50)
    st.write(f"Minat Anda: {interest}%")
    st.write("")
    # Contoh: Video edukasi tambahan
    st.subheader("Mengapa kita harus belajar tentang Jaringan dan Telekomunikasi?")
    st.video("https://youtu.be/Jihg61nafgE?si=nq1LRDF4qLYH00GI")
    
    st.divider()
else:
    st.title(st.session_state.page)


if st.session_state.page == "Daftar Anggota Kelompok":
    show_anggota()
elif st.session_state.page == "Pengertian dan Manfaat Jaringan":
    show_pengertian()
elif st.session_state.page == "Jenis-Jenis Jaringan Komputer":
    show_jenis()
elif st.session_state.page == "Keamanan dan Ancaman Jaringan":
    show_keamanan()
elif st.session_state.page == "Latihan Soal":
    show_latihan()
elif st.session_state.page == "Dokumentasi Kegiatan":
    show_dokumentasi()