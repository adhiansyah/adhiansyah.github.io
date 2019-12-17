---
title: "Aplikasi Streaming Radio dengan Kotlin"
layout: post
author: "Adhiansyah Ancha"
categories: blog
---

Awalnya saya anggap wajar kalau dulu (Android 4 kalau gak salah) ponsel memiliki antena untuk mencari gelombang radio. Kemudian mulai bingung ketika muncul aplikasi radio tanpa membutuhkan _interface_ apapun. Akhirnya saya mengetahui konsep _streaming_ pada aplikasi radio. Lalu saya bertanya-tanya apakah aplikasi ini pakai gelombang FM? 

Ternyata tidak. Mereka menggunakan peladen _streaming_ dengan URL yang unik. Dengan URL tersebut mereka menggunakannya sebagai sumber _streaming_ radio.

Membuat aplikasi _streaming_ radio dalam Kotlin memiliki tantangan. Referensi aplikasi _streaming_ yang saya temui adalah sumber kode Java dan API yang sudah usang, sehingga saya harus berusaha menyesuaikannya dengan spesifikasi Kotlin yang ada.

Mari kita mulai.

Buat proyek baru dengan _Activity_ kosong. Dengan _Activity_ sebagai komponen aplikasi, kita bisa dengan mudah memanggil `findViewById()` untuk merepresentasikan widget kita dalam layout _Activity_. 

```Java
class MainActivity : AppCompatActivity(), View.OnClickListener {
    private var sumberStreaming: String = "http://127.0.0.1:8000"
    private lateinit var putarRadio: FloatingActionButton
    private lateinit var jedaRadio: FloatingActionButton
    private lateinit var pemutarMedia: MediaPlayer
    ...
    ...
    /* Panggil fungsi ini di onCreate() */
    private fun inisialisasi() {
        putarRadio = findViewById(R.id.fabPutar)
        putarRadio.setOnClickListener(this)

        jedaRadio = findViewById(R.id.fabJeda)
        jedaRadio.isEnabled = false
        jedaRadio.setOnClickListener(this)
    }
```

Apabila menggunakan _Fragment_, kita perlu memanggil `view.findViewById()` atau kalau terdapat `inflater`:
```Java
class FirstFragment : Fragment() {
    private var param1: String? = null
    private var param2: String? = null
    private var listener: OnFragmentInteractionListener? = null

    override fun onCreateView(inflater: LayoutInflater,
                              container: ViewGroup?, savedInstanceState: Bundle?): View? {

    /*Bungkus inflater-nya menjadi inisialisasi variabel*/
    val v: View = inflater.inflate(R.layout.fragment_first, container, false)
    ...
    return v    /* Jangan lupa untuk di-return */
```



