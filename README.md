Nama : Qisthan Albani Fasyah

NPM : 2506621434

Kelas : PBP B

### TUGAS 1
1. Iya, Saya menggunakan elemen semantik `<section>`. Ini bertujuan untuk menstruktur bagian web agar terlihat lebih rapi. Selain itu juga untuk mempermudah dalam membaca kode, karena `<section>` sendiri seperti mengandung makna yaitu pemisahan bagian-bagian pada web.
2. Tantangan letak yang saya temukan adalah ketika responsive bagian `<section>` yang saya buat sama percis dengan tampilan di desktop, sehingga saya memodifikasi di bagian @media untuk membuat tampilan kebawah agar menyesuaikan dengan tampilan mobile.
3. Untuk saya sendiri batasan static web ini belum terasa bagi saya karna masih hanya menambahkan section saja tanpa membuatnya dinamis.

Saya menggunakan AI untuk mengerjakan css dan html itu sendiri. pada bagian css karna saya masih belum mengerti bagian desain, sehingga saya pada bagian ini menggunakan full AI. pada bagian html, saya menggunakan AI di bagian portfolio.column karna saya masih tidak mengerti cara membagi kolom itu sendiri.

## TUGAS 2
1. Saat halaman dibuka, request masuk ke urls.py project dan diteruskan ke urls.py aplikasi. Setelah itu, view mengambil data dari model, lalu mengirimkannya ke template. Template mengubah data tersebut menjadi HTML dan hasilnya ditampilkan di browser.
2. Data lebih baik disimpan di model supaya tidak perlu mengubah template setiap kali ada perubahan data. Jadi, data lebih gampang dikelola dan aplikasi juga lebih mudah dikembangkan.
3. makemigrations digunakan untuk membuat migration setelah ada perubahan pada model. Sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database. Contohnya saat menambahkan model Organization, kita menjalankan kedua perintah tersebut agar tabel Organization dibuat di database.

Saya menggunakan AI pada beberapa bagian di Tugas 2, terutama untuk membantu memahami dan menerapkan konsep MVT pada Django. Saya menggunakan AI untuk membantu pada bagian model, view, urls, template, dan unit testing karena saya masih belum terlalu mengerti alur kerja Django. Setelah itu, saya menyesuaikan kembali kode yang diberikan AI dengan kebutuhan tugas saya.

## TUGAS 4
Saya menggunakan AI ChatGPT pada beberapa bagian di Tugas 4 untuk membantu saya memahami penerapan authentication dan authorization pada Django. AI membantu saya dalam memahami penggunaan login, logout, Django Group, role Editor, permission, serta pengaturan hak akses pada fitur Project. Karena saya masih belajar mengenai sistem authentication dan authorization di Django, saya menggunakan ChatGPT sebagai bantuan untuk memahami alur dan memperbaiki kode yang mengalami kendala. Setelah itu, saya menyesuaikan kode tersebut dengan kebutuhan tugas dan melakukan pengecekan pada setiap role untuk memastikan fitur berjalan sesuai ketentuan.

### TUGAS 5
1. Debouncing merupakan teknik untuk menunggu user selesai mengetik sebelum mengirim request ke server. Teknik ini berguna agar request AJAX tidak terlalu banyak dan pencarian menjadi lebih efisien.
2. await digunakan untuk menunggu proses fetch() selesai sebelum lanjut ke kode berikutnya. Jika tidak memakai await, hasil fetch() masih berupa Promise sehingga data belum bisa langsung digunakan.
3. XSS (Cross-Site Scripting) adalah serangan yang memanfaatkan script berbahaya yang dimasukkan ke dalam website. Pada AJAX, kita perlu lebih hati-hati karena data dimasukkan ke halaman menggunakan JavaScript. Jika menggunakan innerHTML secara langsung, script tersebut bisa ikut dijalankan. Oleh karena itu, kita bisa menggunakan textContent dan melakukan validasi data di server.

Saya menggunakan AI ChatGPT pada beberapa bagian di Tugas 5 untuk membantu saya memahami penerapan AJAX dan JavaScript pada Django. AI membantu saya dalam memahami penggunaan fetch(), JSON, debouncing, modal, toast, serta validasi dan pencegahan XSS. Karena saya masih belajar mengenai penggunaan AJAX dalam Django, saya menggunakan ChatGPT sebagai bantuan untuk memahami alur dan memperbaiki kode yang mengalami kendala. Setelah itu, saya menyesuaikan kembali kode tersebut dengan kebutuhan tugas dan melakukan pengecekan pada setiap fitur untuk memastikan semuanya berjalan sesuai ketentuan.