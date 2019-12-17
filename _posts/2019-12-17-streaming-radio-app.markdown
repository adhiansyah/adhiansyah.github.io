---
title: "Membuat Aplikasi Streaming Radio dengan Android Studio"
layout: post
author: "Adhiansyah Ancha"
categories: blog
---

Selamat datang di pos pertama weblog ini. Kali ini saya akan menuliskan tentang cara menerapkan _streaming_ radio dengan Android Studio. Pos saya ini lebih menekankan kepada pencatatan referensi saja, bukan tahap-tahap menerapkannya. Karena itu mungkin para pembaca kesulitan harus mulai dari mana.

_Streaming_ radio bisa dijalankan hanya dengan 2 tombol _FloatingActionButton_ (mulai dan jeda). Saya menemukan bahwa ketika tombol mulai memproses _streaming_, dan tiba-tiba pengguna menekan tombol jeda, hal yang terjadi adalah `prepareAsync()` (inisisasi streaming pada tombol mulai) berhenti pada keadaan 4 (memproses).

Ini akan mengakibatkan bila pengguna menekan tombol mulai lagi, aplikasi akan tiba-tiba keluar tanpa ada pemberitahuan. Dalam log Android Studio, ini ditandai dengan pelemparan error `java.lang.IllegalStateException at android.media.MediaPlayer.prepareAsync(Native Method)`.

