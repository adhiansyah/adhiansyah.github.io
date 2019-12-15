---
layout: default
---

# Selamat datang di weblog saya
Petama kali dibuat pada 24 November 2018, saya baru mengubah total tampilan weblog saya pada 15 Desember 2019 karena tidak ada waktu yang tepat untuk mengubah dan pada waktu itu saya agak bosan dengan teknologi web.

[Percobaan](./another-page.html).

## Pengujian berbagai fitur "Hacker"

# Kutipan favorit
> Orang-orang berpikir komputer akan mencegah mereka membuat kesalahan. Mereka salah. 
> Dengan komputer, Anda membuat kesalahan lebih banyak
>                  
> - Adam Osborne


# Salah satu tampilan potongan kode
```cpp
// Baris 1276 hingga 1306 dari berkas <cpu.c> di Kernel Linux
void enable_nonboot_cpus(void)
{
	int cpu, error;

	/* Allow everyone to use the CPU hotplug again */
	cpu_maps_update_begin();
	__cpu_hotplug_enable();
	if (cpumask_empty(frozen_cpus))
		goto out;

	pr_info("Enabling non-boot CPUs ...\n");

	arch_enable_nonboot_cpus_begin();

	for_each_cpu(cpu, frozen_cpus) {
		trace_suspend_resume(TPS("CPU_ON"), cpu, true);
		error = _cpu_up(cpu, 1, CPUHP_ONLINE);
		trace_suspend_resume(TPS("CPU_ON"), cpu, false);
		if (!error) {
			pr_info("CPU%d is up\n", cpu);
			continue;
		}
		pr_warn("Error taking CPU%d up: %d\n", cpu, error);
	}

	arch_enable_nonboot_cpus_end();

	cpumask_clear(frozen_cpus);
out:
	cpu_maps_update_done();
}
```

#### H4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### H5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### H6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |