from flask import Flask, render_template, abort

app = Flask(__name__)

# Bütün kurs səviyyələri və onların detallı tədris proqramı (silabus)
KURS_DATA = {
    "ilkin": {
        "ad": "İlkin Anlayışlar (Beginner)",
        "aciqlama": "Şəbəkə əsasları, Linux (Kali Linux) introduksiya, təməl kiber təhlükəsizlik terminləri və mentaliteti.",
        "reng": "success",
        "proqram": [
            "Kiber Təhlükəsizliyə Giriş və Mentalitet",
            "Şəbəkə Əsasları (OSI Modeli, TCP/IP, IP və MAC ünvanları)",
            "Linux Əməliyyat Sistemi (Kali Linux quraşdırılması və təməl komandalar)",
            "İnformasiya Təhlükəsizliyinin Üçbucağı (CIA Triad: Confidentiality, Integrity, Availability)",
            "Sosial Mühəndislik (Social Engineering) və Fishing hücumlarının məntiqi"
        ]
    },
    "orta": {
        "ad": "Orta Səviyyə (Intermediate)",
        "aciqlama": "Sızma testləri (Penetration Testing), Nmap ilə skanlama, Metasploit, Burp Suite ilə Web App təhlükəsizliyi.",
        "reng": "warning",
        "proqram": [
            "Sızma Testlərinin (Penetration Testing) Mərhələləri",
            "Nmap ilə Aktiv/Passiv Kəşfiyyat və Şəbəkə Skanlaması",
            "Metasploit Framework ilə Sistem Boşluqlarının Tapılması və Eksploytasiya",
            "Web Proqram Təhlükəsizliyi (OWASP Top 10, SQL Injection, XSS)",
            "Şəbəkə Trafikinin Analizi və Wireshark istifadəsi"
        ]
    },
    "ileri": {
        "ad": "İləri Səviyyə (Advanced)",
        "aciqlama": "Exploit hazırlanması, Python ilə kiber alətlərin proqramlaşdırılması, Red Teaming və İnstitusional qorunma.",
        "reng": "danger",
        "proqram": [
            "İləri Səviyyə Eksploytasiya və Buffer Overflow əsasları",
            "Python Proqramlaşdırma ilə Xüsusi Kiber Alətlərin (Skanerlər, Snifferlər) Yazılması",
            "Red Teaming və Blue Teaming Ssenariləri (Hücum və Müdafiə)",
            "Active Directory Təhlükəsizliyi və Korporativ Şəbəkələrə Sızma",
            "Zərərli Proqramların (Malware) Analizi və Antiviruslardan Yayınma Texnikaları"
        ]
    }
}

# 1. Ana Səhifə
@app.route('/')
def index():
    kurs_melumat = {
        "ad": "IsoProtection Tədris Mərkəzi",
        "tesvir": "Gələcəyin Kiber Təhlükəsizlik Mütəxəssislərini Yetişdiririk. Praktiki laboratoriyalar (Kali Linux, Metasploit) və real ssenarilərlə tədris.",
        "elaqe": "+994 (10) 324-87-24",
        "email": "isomprotection@gmail.com"
    }
    return render_template('index.html', kurs=kurs_melumat)

# 2. "Kursa Başla" Səhifəsi (Səviyyə seçimləri)
@app.route('/kursa-basla')
def kursa_basla():
    # KURS_DATA lüğətindən məlumatları HTML-ə göndəririk
    seviyyeler = []
    for k, v in KURS_DATA.items():
        seviyyeler.append({
            "id": k,
            "ad": v["ad"],
            "aciqlama": v["aciqlama"],
            "reng": v["reng"]
        })
    return render_template('kurs.html', seviyyeler=seviyyeler)

# 3. Kurs Detay Səhifəsi (YENİ ROUTE)
@app.route('/kurs/<seviyye_id>')
def kurs_detay(seviyye_id):
    if seviyye_id in KURS_DATA:
        seviyye = KURS_DATA[seviyye_id]
        return render_template('kurs_detay.html', seviyye=seviyye)
    else:
        abort(404) # Səhv ID yazılarsa 404 xətası ver

# 4. Kali Linux Alətləri Səhifəsi
@app.route('/tools')
def tools():
    kali_tools = [
        {
            "id": "nmap",
            "ad": "Nmap (Network Mapper)",
            "kateqoriya": "Şəbəkə Skanlanması və Kəşfiyyat",
            "aciqlama": "Hədəf sistemlərdə açıq portları, işləyən servisləri və əməliyyat sistemini təyin etmək üçün istifadə olunan ən güclü şəbəkə skaneridir.",
            "komanda": "nmap -sV -O <hədəf_ip>"
        },
        {
            "id": "metasploit",
            "ad": "Metasploit Framework",
            "kateqoriya": "Exploitation (Sızma)",
            "aciqlama": "Sistemlərdəki boşluqları (vulnerability) yoxlamaq və tapılan boşluqlardan istifadə edərək sistemə sızmaq (exploit etmək) üçün istifadə edilən platformadır.",
            "komanda": "msfconsole"
        },
        {
            "id": "burpsuite",
            "ad": "Burp Suite",
            "kateqoriya": "Web Proqram Təhlükəsizliyi",
            "aciqlama": "Veb saytların təhlükəsizliyini yoxlamaq üçün proxy rolunu oynayan alətdir. Brauzer ilə server arasındakı sorğuları tutur, analiz edir və dəyişdirir.",
            "komanda": "burpsuite"
        },
        {
            "id": "wireshark",
            "ad": "Wireshark",
            "kateqoriya": "Trafik Analizi (Sniffing)",
            "aciqlama": "Şəbəkə daxilində ötürülən məlumat paketlərini real vaxt rejimində tutub analiz etmək (sniffing) üçün istifadə olunan ən populyar protokol analizatorudur.",
            "komanda": "wireshark"
        },
        {
            "id": "john",
            "ad": "John the Ripper",
            "kateqoriya": "Şifrə Qırma (Password Cracking)",
            "aciqlama": "Sistemlərdən əldə edilmiş şifrə hash-lərini (məsələn, MD5, SHA-256) brute-force (kobud qüvvə) və lüğət hücumları ilə qırmaq üçün istifadə olunur.",
            "komanda": "john --wordlist=pass.txt hash.txt"
        }
    ]
    return render_template('tools.html', tools=kali_tools)

if __name__ == '__main__':
    app.run(debug=True)