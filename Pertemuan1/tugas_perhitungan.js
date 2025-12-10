// variabel awal
let tombol_cek = document.getElementById('tombol');
let i = 0
let data_history = [];
let total_nilai_input = 0;

function tugas_1() {
    let data_input = Number(document.getElementById('input').value);
    let output = document.getElementById('output');
    data_history.push(data_input);

    // i++ menambah hitungan +1 jika tombol diklik
    i++

    // menampilkan output seudah tombolnya diklik
    output.innerHTML += `Masukkan angka ke-${i}: ${data_history[i-1]} <br>`

    // menjumlahkan total nilai input setiap klikan
    total_nilai_input += data_history[i-1]

    // jika total nilai inputan lebih dari 100 maka selesai
    if (total_nilai_input > 100) {
        tombol_cek.disabled = true;
        output.innerHTML += `<br> SELESAI. TOTAL = ${total_nilai_input}`
    }
}

// pembaca, jika tombol cek diklik maka fungsi tugas_1 dijalankan
tombol_cek.addEventListener('click', tugas_1);