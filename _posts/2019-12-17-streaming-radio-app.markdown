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

1. Buat proyek baru dengan _Activity_ kosong. Saya menambahkan 2  _FloatingActionButton_ dalam layout `activity_main.xml` dengan nama ID `fabPutar` dan `fabJeda`. Bisa disesuaikan sesuai kebutuhan
```XML
<com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fabPutar" 
        android:layout_width="68dp"
        android:layout_height="55dp"
        android:layout_marginStart="240dp"
        android:layout_marginTop="168dp"
        android:layout_marginEnd="130dp"
        android:layout_marginBottom="202dp"
        android:clickable="true"
        android:focusable="true"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="parent"
        app:srcCompat="@android:drawable/ic_media_play" />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fabJeda"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="100dp"
        android:layout_marginTop="168dp"
        android:layout_marginEnd="82dp"
        android:layout_marginBottom="201dp"
        android:clickable="true"
        android:focusable="true"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toStartOf="parent"
        app:layout_constraintHorizontal_bias="0.0"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="parent"
        app:srcCompat="@android:drawable/ic_media_pause" />
```

2. Saya akan menggunakan `MainActivity` sebagai dasar antarmuka  _streaming_ radio:

