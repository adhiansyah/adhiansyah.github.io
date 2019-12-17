---
title: "Aplikasi Streaming Radio dengan Kotlin"
layout: post
author: "Adhiansyah Ancha"
categories: blog
---

Awalnya saya anggap wajar kalau dulu (Android 4 kalau gak salah) ponsel memiliki antena untuk mencari gelombang radio. Kemudian mulai bingung ketika muncul aplikasi radio tanpa membutuhkan _interface_ apapun. Akhirnya saya mengetahui konsep _streaming_ pada aplikasi radio. Lalu saya bertanya-tanya apakah aplikasi ini pakai gelombang FM? 

Ternyata tidak. Mereka menggunakan peladen _streaming_ dengan URL yang unik. Dengan URL tersebut mereka menggunakannya sebagai sumber _streaming_ radio.

Membuat aplikasi _streaming_ radio dalam Kotlin memiliki tantangan. Referensi aplikasi _streaming_ yang saya temui adalah sumber kode Java dan API yang sudah usang, sehingga saya harus berusaha menyesuaikannya dengan spesifikasi Kotlin yang ada.

--

Dengan _Activity_ sebagai komponen aplikasi, kita bisa dengan mudah memanggil `findViewById()` untuk merepresentasikan widget kita dalam layout _Activity_. 

```Kotlin

```

Apabila menggunakan _Fragment_, kita perlu memanggil `view.findViewById()` atau kalau terdapat `inflater`, kita bisa me



