
// Inisiasi inputan data
let tombol_cek = document.getElementById('tombol');
let k = 0
let data_history = [];

// Fungsi
function latihan_1() {
    let data_input = Number(document.getElementById('angka').value);
    let output = document.getElementById('output');
    data_history.push(data_input);

    // Kondisi
    if (data_input === 999) {
        output.innerHTML = `ANDA BERHASIL pada percobaan ke-${k++ +1}`
        tombol_cek.disabled = true;

        // Untuk menampilkan riwayat inputan
        for (let i = 0; i < data_history.length; i++) {
            output.innerHTML += `<br> Tebakan ke-${i+1}: ${data_history[i]}`;
        }
    } else {
        output.innerHTML = `Maaf salah`
        console.log(k++);
    }
}

tombol_cek.addEventListener('click', latihan_1);