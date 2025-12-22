
import pandas as pd
import os

def run_preprocessing():
    # 1. Tentukan folder sumber (raw) dan tujuan (preprocessing)
    raw_dir = 'namadataset_raw'
    output_dir = 'preprocessing/namadataset_preprocessing'
    
    # Buat folder jika belum ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f" Membuat folder: {output_dir}")

    # 2. Path file (Sesuaikan dengan nama file CSV mentah Anda)
    # Kita cari file csv apapun di dalam folder raw
    try:
        raw_files = [f for f in os.listdir(raw_dir) if f.endswith('.csv')]
        if not raw_files:
            print("Tidak ada file CSV di folder namadataset_raw")
            return
        
        raw_path = os.path.join(raw_dir, raw_files[0])
        print(f"Membaca data dari: {raw_path}")
        df = pd.read_csv(raw_path)

        # 3. PROSES PREPROCESSING (Sesuai eksperimen Mirananda)
        # Menyeragamkan kolom
        df.columns = [col.lower() for col in df.columns]
        
        # Contoh cleaning: menghapus baris kosong
        df = df.dropna()
        
        # 4. Simpan hasil
        output_path = os.path.join(output_dir, 'youtube_preprocessed.csv')
        df.to_csv(output_path, index=False)
        print(f"BERHASIL! Data tersimpan di: {output_path}")
        print(f"Jumlah data: {len(df)} baris")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == '__main__':
    run_preprocessing()
