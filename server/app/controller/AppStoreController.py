from app.model.post import Posts
from app.model.api_config import API_Config
from app.model.word_cloud import Word_Clouds
from app.model.user import Users
from app import response, app
from flask import request
import requests
from app import db
from datetime import datetime
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from sklearn import svm
from sklearn.metrics import classification_report
import pandas as pd
from pandas import DataFrame
import jsonify
from sklearn import naive_bayes
import numpy as np
import nltk
import re
from nltk.tokenize import RegexpTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from googletrans import Translator
import collections
from sqlalchemy.sql import func
from flask_jwt_extended import *
import xml.etree.ElementTree as ET



def model_svm(test_data):
    temp = []
    data_posts = Posts.query.all()
    neg_count = Posts.query.filter(Posts.sentiment==0).count()
    pos_count = Posts.query.filter(Posts.sentiment==1).count()
    # train data
    if(len(data_posts) / 2 > len(test_data) and neg_count != 0 and pos_count != 0):
        for data in data_posts:
            temp.append({ "text": data.post, "is_positive": data.sentiment })
        trainData = DataFrame(temp,columns=['text', 'is_positive'], dtype=object)
    else:
        trainData = pd.read_csv("https://raw.githack.com/Jodyheryanto/testing_sentiment/master/dataset_keseluruhan_train.csv")
    #test data
    testData = DataFrame(test_data,columns=['post'], dtype=object) 
    #preprocessing
    trainData['text'] = trainData['text'].apply(preprocess_text)
    testData['post'] = testData['post'].apply(preprocess_text)

    # Create feature vectors
    vectorizer = TfidfVectorizer(use_idf = True)

    train_vectors = vectorizer.fit_transform(trainData['text'])
    test_vectors = vectorizer.transform(testData['post'])

    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    classifier_linear.fit(train_vectors, trainData['is_positive'].astype('int64'))
    prediction_linear = classifier_linear.predict(test_vectors)
    return prediction_linear

def preprocess_text(review):
    appos = {
    "thankyou":"terimakasih",
    "dikasi":"beri",
    "tau":"tahu",
    "gabisa":"tidak bisa",
    "gaada":"tidak ada",
    "lg":"lagi",
    "gada":"tidak ada",
    "pake":"pakai",
    "bnr":"benar",
    "klo":"kalau",
    "dmn":"dimana",
    "dapet":"dapat",
    "nanya":"tanya",
    "dipake":"pakai",
    "emang":"memang",
    "okay":"ya",
    "thx":"terimakasih",
    "tq":"terimakasih",
    "sngt":"sangat",
    "sgt":"sangat",
    "bgtttt":"sangat",
    "bngt":"sangat",
    "jln":"jalan",
    "naek":"naik",
    "tokped":"tokopedia",
    "belom":"belum",
    "kemaren":"kemarin",
    "liat":"lihat",
    "topup":"top up",
    "account":"akun",
    "mantul":"mantap",
    "discount":"diskon",
    "sdh":"sudah",
    "duit":"uang",
    "karna":"karena",
    "wagelaseh":"mantap",
    "pesen":"pesan",
    "rebu":"ribu",
    "simple":"simpel",
    "best":"bagus",
    "lope":"suka",
    "lgi":"lagi",
    "krna":"karena",
    "drpd":"daripada",
    "hepi":"senang",
    "thanks":"terimakasih",
    "buy":"beli",
    "disc":"diskon",
    "shopping":"belanja",
    "milih":"pilih",
    "trs":"terus",
    "bnyak":"banyak",
    "untung pake":"untung pakai",
    "sudh":"sudah",
    "udh":"sudah",
    "nikmatin":"nikmat",
    "temanteman":"teman teman",
    "back":"kembali",
    "perjalan":"perjalanan",
    "cashkembali":"cash kembali",
    "gampah":"mudah",
    "sampe":"sampai",
    "temen":"teman",
    "pakaik":"pakai",
    "pke":"pakai",
    "mantab":"mantap",
    "ngtidak":"tidak",
    "enggak":"tidak",
    "ngga": "tidak",
    "nga": "tidak",
    "ga": "tidak",
    "trus":"terus",
    "jalanjalan":"jalan jalan",
    "jdi":"jadi",
    "cashkembalinya":"cash kembali",
    "anter":"antar",
    "gaperlu":"tidak perlu",
    "emak":"ibu",
    "cepet":"cepat",
    "kmn":"kemana",
    "gabawa":"tidak bawa",
    "gausah":"tidak perlu",
    "byr":"bayar",
    "lagii":"lagi",
    "dehh":"deh",
    "bnyk":"banyak",
    "ntidak":"tidak",
    "smemangat":"semangat",
    "thank":"terimakasih",
    "deket":"dekat",
    "engga":"tidak",
    "menikmat":"menikmati",
    "mw":"mau",
    "bangettt":"sangat",
    "smpe":"sampai",
    "ojol":"ojek online",
    "terkejoed":"terkejut",
    "kmana":"kemana",
    "thx":"terimakasih",
    "ajaa":"saja",
    "cuss":"pergi",
    "mempersudah":"mudah",
    "bnget":"sangat",
    "hematt":"hemat",
    "hemattt":"hemat",
    "beliin":"beli",
    "smenjak":"semenjak",
    "bangett":"sangat",
    "terusss":"terus",
    "maap":"maaf",
    "irittt":"irit",
    "mantep":"mantap",
    "ajah":"saja",
    "ampe":"sampai",
    "murahhh":"murah",
    "mayan":"lumayan",
    "lbih":"lebih",
    "hrs":"harus",
    "gilaaa":"gila",
    "bangeet":"sangat",
    "maen":"main",
    "skrng":"sekarang",
    "ortu":"orang tua",
    "gmn":"bagaimana",
    "klau":"kalau",
    "gilak":"gila",
    "semanjak":"semenjak",
    "lagisg":"lagi",
    "horang":"orang",
    "bangetttt":"sangat",
    "dateng":"datang",
    "bwt":"buat",
    "macem":"macam",
    "brooo":"bro",
    "nyangka":"sangka",
    "restahurant":"restoran",
    "bingits":"sangat",
    "bisaaaaaaa":"bisa",
    "murce":"murah",
    "pkek":"pakai",
    "cmn":"Cuma",
    "kmna":"kemana",
    "kyk":"seperti",
    "untungpakai":"untung pakai",
    "gegara":"karena",
    "slalu":"selalu",
    "pinter":"pintar",
    "garibet":"tidak ribet",
    "makai":"pakai",
    "mesan":"pesan",
    "mevvah":"mewah",
    "ilang":"hilang",
    "mna":"mana",
    "iritt":"irit",
    "guyss":"guys",
    "murmer":"murah",
    "mantabl":"mantap",
    "gapernah":"tidak pernah",
    "kenyaaang":"kenyang",
    "maksi":"makan siang",
    "anakanak":"anak anak",
    "bgd":"sangat",
    "nggk":"tidak",
    "lage":"lagi",
    "ksana":"kesana",
    "muraaaah":"murah",
    "trimakasih":"terimakasih",
    "dooong":"dong",
    "hemaaat":"hemat",
    "jadii":"jadi",
    "demen":"suka",
    "bkin":"buat",
    "ttp":"tetap",
    "laen":"lain",
    "markotop":"sangat",
    "hemaaaaat":"hemat",
    "jugaa":"juga",
    "iritttt":"irit",
    "bgtt":"sangat",
    "banget":"sangat",
    "bangeeet":"sangat",
    "skolah":"sekolah",
    "ngirim":"kirim",
    "bosen":"bosan",
    "iyaa":"iya",
    "caskembali":"cash kembali",
    "kawatir":"khawatir",
    "wahh":"wah",
    "hbs":"habis",
    "abisabis":"habis",
    "makanmakan":"makan makan",
    "melulu":"selalu",
    "apalagii":"apalagi",
    "bangettttt":"sangat",
    "lhooo":"lho",
    "guysburuan":"guys buruan",
    "sekarg":"sekarang",
    "dlu":"dulu",
    "rmh":"rumah",
    "ksini":"kesini",
    "sekalehhhhh":"sekali",
    "mantabh":"mantap",
    "hematmau":"hemat mau",
    "blnja":"belanja",
    "semnjak":"semenjak",
    "brani":"berani",
    "pasan":"pesan",
    "mantabll":"mantap",
    "pulak":"pula",
    "banged":"sangat",
    "muraaah":"murah",
    "dipermsudah":"mudah",
    "grgr":"garagara",
    "gapunya":"tidak punya",
    "benarbenar":"benar benar",
    "kluar":"keluar",
    "murahhhhh":"murah",
    "bangat":"sangat",
    "kdg":"kadang",
    "oake":"oke",
    "skarang":"sekarang",
    "ajaaa":"aja",
    "ramerame":"rame",
    "gausa":"tidak perlu",
    "gatahu":"tidak tahu",
    "dimsudahkan":"mudah",
    "katidak":"tidak",
    "perantahuan":"rantau",
    "brangkat":"berangkat",
    "knp":"kenapa",
    "trima":"terima",
    "itungitung":"hitung",
    "bingit":"sangat",
    "goodluck":"good luck",
    "khwatir":"khawatir",
    "mmg":"memang",
    "bangeeeet":"sangat",
    "guysssss":"guys",
    "irittttt":"irit",
    "diskonon":"diskon",
    "hematnyaa":"hemat",
    "muraah":"murah",
    "terimakasihh":"terimakasih",
    "seneng":"senang",
    "semejak":"semenjak",
    "antarin":"antar",
    "kuatir":"khawatir",
    "malem":"malam",
    "sangattt":"sangat",
    "siangmal":"siang",
    "rame":"ramai",
    "sangatt":"sangat",
    "food":"makan",
    "lulumayan":"lumayan",
    "gooduluck":"good luck",
    "luv":"love",
    "love":"suka",
    "ngluarin":"keluar",
    "muluu":"mulu",
    "byebye":"bye",
    "gampang":"mudah",
    "terimakasi":"terimakasih",
    "terimakasihh":"terimakasih",
    "point":"poin",
    "gak":"tidak",
    "nggak":"tidak",
    "ngak":"tidak",
    "kagak":"tidak",
    "gakk":"tidak",
    "gede":"besar",
    "bokekbtl":"bokek",
    "kekinian":"hits",
    "ngerti":"tahu",
    "rantahu":"rantau",
    "smuanya":"semua",
    "smnjak":"semenjak",
    "smakin":"semakin",
    "smg":"semoga",
    "paspesan":"cukup",
    "murahh":"murah",
    "hematt":"hemat",
    "pny":"punya",
    "pnya":"punya",
    "gilakk":"gila",
    "tidakk":"tidak",
    "anggaran":"biaya",
    "gilaa":"gila",
    "buruburu":"buru buru",
    "rbu":"ribu",
    "emol":"mall",
    "promoaa":"promo",
    "promopromo":"promo promo",
    "mol":"mall",
    "dahsyat":"mantap",
    "sya":"saya",
    "custumer":"customer",
    "tmn":"teman",
    "mantapp":"mantap",
    "doangg":"doang",
    "kaga":"tidak",
    "mantapl":"mantap",
    "ngtidak":"tidak",
    "berlipatlipat":"berlipat",
    "kocek":"dompet",
    "euyyy":"euy",
    "ngtidak":"tidak",
    "gtidakman":"tidak",
    "terimakasihu":"terimakasih",
    "kosterimakasih":"terimakasih",
    "mmemang":"memang",
    "hhilang":"hilang",
    "ibuibu":"ibu ibu",
    "bhilang":"bilang",
    "sangking":"saking",
    "dekatdengan":"dekat dengan",
    "gengsss":"guys",
    "jelong":"jalan",
    "dongg":"dong",
    "sangatss":"sangat",
    "nongki":"nongkrong",
    "gretong":"gratis",
    "kmemang":"kemang",
    "bangget":"banget",
    "senanggg":"senang",
    "pesang":"pesan",
    "seringsering":"sering sering",
    "tengkyu":"terimakasih",
    "lngsung":"langsung",
    "semangatmau":"semangat mau",
    "sangatapalagi":"sangat apalagi",
    "emng":"memang",
    "akte":"akta",
    "bp":"bapak",
    "sampe":"sampai",
    "sayarat":"syarat",
    "berlakun":"berlaku",
    "masayarakat":"masyarakat",
    "dukcapil":"dispenduk",
    "dispendukcapil":"dispenduk",
    "blanko":"blangko",
    "kawin":"nikah",
    "mksh":"makasih",
    "prihal":"perihal",
    "adminitrasi":"administrasi",
    "dispendukpenduk":"dispenduk",
    "dispendukdispenduk":"dispenduk",
    "dispendispenduk":"dispenduk",
    "sy":"saya",
    "sdh":"sudah",
    "bbrp":"beberapa",
    "utk":"untuk",
    "mhn":"mohon",
    "org":"orang",
    "olh":"oleh",
    "yg":"yang",
    "jg":"juga",
    "kpd":"kepada",
    "tgl":"tanggal",
    "bln":"bulan",
    "sm":"sama",
    "dg":"dengan",
    "sby":"surabaya",
    "bhwa":"bahwa",
    "bhw":"bahwa",
    "lgi":"lagi",
    "msh":"masih",
    "ats":"atas",
    "jl":"jalan",
    "aka1":"kartukuning",
    "kartu kuning":"kartukuning",
    "kartu tanda pencari kerja":"kartukuning",
    "kartu pencari kerja":"kartukuning",
    "nggu":"nunggu",
    "slesei":"selesai",
    "dgn":"dengan",
    "bgtu":"begitu",
    "bgt":" sangat",
    "banget":" sangat",
    "suket":"surat keterangan",
    "trima":"terima",
    "trm":"terima",
    "polisi tidur":"speedtrap",
    "pd":"pada",
    "kmarin":"kemarin",
    "kmrn":"kemarin",
    "gg":"gang",
    "lht":"lihat",
    "puskesamaas":"puskesmas",
    "stelah":"setelah",
    "manganga":"mangga",
    "ersayaaratan":"persyaratan",
    "sdengankan":"sedangkan",
    "airlanganga":"airlangga",
    "psyarat":"persyaratan",
    "ditunungangu":"ditunggu",
    "menunungangu":"menunggu",
    "sekal":"sekali",
    "risamaa":"risma",
    "terimaksih":"terimakasih",
    "pendafarannya":"pendaftarannya",
    "sehinganga":"sehingga",
    "bapakkb":"bapak",
    "masayarkat":"masyarakat",
    "ktpel":"ktp",
    "carany":"caranya",
    "prsetujuan":"persetujuan",
    "selanjutny":"selanjutnya",
    "infonyaaaaaaa":"infonya",
    "cpt":"cepat",
    "apalag":"apalagi",
    "tlagi":"lagi",
    "tinngi":"tinggi",
    "adlh":"adalah",
    "kksaya":"kk",
    "shilang":"hilang",
    "selsai":"selsai",
    "trdaftar":"terdaftar",
    "trnyata":"ternyata",
    "teralalu":"terlalu",
    "meingangalkan":"meninggalkan",
    "keajadiyan":"kejadian",
    "metanyakan":"menanyakan",
    "kasihadministrasi":"administrasi",
    "menungangunakan":"menggunakan",
    "lobang":"lubang",
    "berlobang":"berlubang",
    "harga":"biaya",
    "tangangapan":"tanggapan",
    "ppersyaratan":"persyaratan",
    "sayaarat":"syarat",
    "pagisurat":"surat",
    "upadaate":"update",
    "caranyaa":"caranya",
    "ktpunyaa":"ktpnya",
    "sayakenapa":"saya kenapa",
    "sayaarat":"syarat",
    "meningangal":"meninggal",
    "tegalsaridijanjikan":"tegalsari dijanjikan",
    "surabayaterus":"surabaya terus",
    "form":"formulir",
    "masayaarakat":"masyarakat",
    "working":"kerja",
    "bubutandan":"bubutan dan",
    "suwon":"terimakasih",
    "bener":"benar",
    "bagaimanaa":"bagaimana",
    "sblmny":"sebelumnya",
    "yaainfo":"ya info",
    "disdispenduk":"dispenduk",
    "sayaaratnya":"syaratnya",
    "ngurusin":"ngurus",
    "pamanya":"paman",
    "sarat":"syarat",
    "dbuatkan":"dibuatkan",
    "atidak":"tidak",
    "dengann":"dengan",
    "pebgurusan":"pengurusan",
    "srt":"surat",
    "brpa":"berapa",
    "tks":"terimakasih",
    "diknas":"dinas",
    "caranyaamohon":"caranya",
    "amana":"amanah",
    "wargaorang":"warga orang",
    "office":"kantor",
    "minini":"minim",
    "adad":"ada",
    "ditangangapi":"ditanggapi",
    "nungangu":"nunggu",
    "dtang":"datang",
    "ektpnya":"ektp",
    "padahl":"padahal",
    "lejas":"jelas",
    "sekaliian":"sekalian",
    "informulirasinya":"informasi",
    "informulirasi":"informasi",
    "untk":"untuk",
    "ssamapai":"sampai",
    "praktak":"praktik",
    "formulirulir":"formulir",
    "kecamatankk":"kecamatan",
    "dikecamatan":"kecamatan",
    "penungguna":"pengguna",
    "sampa":"sampah",
    "indormasinya":"informasinya",
    "hri":"hari",
    "padan":"padam",
    "kk":"kartukeluarga",
    "gorong":"selokan",
    "goronggorong":"selokan",
    "ektpsaat":"ektp",
    "ewadulada":"ewadul",
    "mndapatkan":"mendapatkan",
    "siangmaaf":"siang maaf",
    "kmbali":"kembali",
    "pasl":"pasti",
    "telp":"telpon",
    "bsa":"bisa",
    "dminta":"diminta",
    "document":"dokumen",
    "laik":"lain",
    "kartukuningnya":"kartukuning",
    "terkahir":"terakhir",
    "notifkasi":"notifikasi",
    "dirw":"rw",
    "sampa":"sampah",
    "dimanaa":"dimana",
    "bantuannya":"bantuan",
    "megurus":"mengurus",
    "sampahil":"sampah",
    "tagangal":"tanggal",
    "tlpn":"telepon",
    "mksih":"makasih",
    "tny":"tanya",
    "almh":"almarhum",
    "nyakin":"yakin",
    "pangangilan":"panggilan",
    "thilang":"tilang",
    "reapon":"respon",
    "tertangangal":"tertanggal",
    "sampahhi":"sampah",
    "prosedurpersyaratan":"prosedur persyaratan",
    "ktpnya":"ktp",
    "kecamatanpetugas":"kecamatan petugas",
    "sampahhh":"sampah",
    "selanjutanyaa":"selanjutnya",
    "melegalisir":"legalisir",
    "makasie":"makasih",
    "berlakuya":"berlakunya",
    "begimana":"bagaimana",
    "debirokratisasi":"birokrasi",
    "public":"publik",
    "service":"pelayanan",
    "pelangangan":"pelanggaran",
    "syaratanyaa":"syarat",
    "assalamualainum":"assalamualaikum",
    "dicetakapakah":"dicetak apakah",
    "dtg":"datang",
    "habistd":"habis",
    "skr":"sekarang",
    "aparteman":"apartemen",
    "slmat":"selamat",
    "salinantarima":"salin",
    "tutidakan":"tiadakan",
    "direspon":"respon",
    "cepatanyaa":"cepat",
    "disepanjang":"sepanjang",
    "kenyamanahn":"kenyamanan",
    "apartment":"apartemen",
    "matimulai":"mati",
    "seoanjang":"sepanjang",
    "padamg":"padam",
    "expired":"mati",
    "expire":"mati",
    "brapa":"berapa",
    "kartukeluargas":"kartukeluarga",
    "pembuatanya":"buat",
    "pengambilanya":"ambil",
    "skali":"sekali",
    "sekarangk":"sekarang",
    "perosedurnya":"prosedur",
    "tetapai":"tetapi",
    "pernyaataan":"pernyataan",
    "ank":"anak",
    "tlng":"tolong",
    "bbagaimana":"bagaimana",
    "selanjutnyaa":"selanjutnya",
    "dftrkan":"daftarkan",
    "dokterbidan":"dokter bidan",
    "disurabaya":"surabaya",
    "pertanyannya":"pertanyaannya",
    "shg":"sehingga",
    "lagis":"lagi",
    "ngangih":"nagih",
    "sunungguh":"sungguh",
    "selsai":"selesai",
    "selesa":"selesai",
    "sampahsampah":"sampah",
    "sampahl":"sampah",
    "sampa":"sampah",
    "sekarangg":"sekarang",
    "diiklanakan":"iklan",
    "pavingisasi":"paving",
    "sesunguhnya":"sesungguhnya",
    "msampaht":"sampah",
    "plihan":"pilihan",
    "slh":"salah",
    "stu":"satu",
    "light":"lampu",
    "pavingnya":"paving",
    "padam":"mati",
    "padaam":"mati",
    "selokananselokan":"selokan",
    "tangap":"tanggap",
    "selokananselokanselokanuntuk":"selokan",
    "agr":"agar",
    "jngn":"jangan",
    "spy":"supaya",
    "bleh":"boleh",
    "samaa":"sama",
    "memasukartukeluargaan":"kartukeluarga",
    "lengkapinsampahh":"sampah",
    "sampahh":"sampah",
    "sampa":"sampah",
    "ngurusnya":"urus",
    "bantuanya":"bantuan",
    "ditandatangani":"tanda tangan",
    "samap":"sama",
    "sdengan":"dengan",
    "sulitanyaa":"sulit",
    "disetujui":"setuju",
    "kelurahannya":"kelurahan",
    "sekal":"sekali",
    "temanaku":"temanku",
    "keluarahan":"kelurahan",
    "sekaliigus":"sekaligus",
    "nomernya":"nomer",
    "kekelurahan":"kelurahan",
    "kartukeluargaini":"kartukeluarga",
    "siolacapek":"siola",
    "baharu":"baru",
    "kartukuninga":"kartukuning",
    "prngamblan":"pengambilan",
    "tingangalnya":"tanggalnya",
    "teimakasih":"terimakasih",
    "melelui":"melalui",
    "samaua":"sama",
    "persayaratannya":"syarat",
    "kelurahaan":"kelurahan",
    "dikecamtan":"kecamatan",
    "kmrin":"kemarin",
    "kntor":"kantor",
    "hrus":"harus",
    "kecamtan":"kecamatan",
    "dikecamtan":"kecamatan",
    "penpanjangnya":"perpanjangan",
    "komputereh":"komputer",
    "selesa":"selesai",
    "samak":"sama",
    "harapanan":"harapan",
    "ragajika":"raga",
    "ragasebenarnya":"raga",
    "ragawan":"raga",
    "pnerangan":"penerangan",
    "tmpat":"tempat",
    "sblm":"sebelum",
    "teribuka":"terbuka",
    "tirtoasr":"tirtoasri",
    "trlalu":"terlalu",
    "membahaykan":"membahayakan",
    "terrealisasi":"terealisasi",
    "gelapcoba":"gelap",
    "nnti":"nanti",
    "sngat":"sangat",
    "mengfasilitasi":"memfasilitasi",
    "mnghindari":"menghindari",
    "ditraffic":"traffic",
    "jpu":"pju",
    "terimaadministrasi":"terima administrasi",
    "yaadministrasi":"ya administrasi",
    "surabayaadministrasi":"surabaya administrasi",
    "telfon": "telepon",
    "y": "ya",
    "the bestttt": "terbaik",
    "the bestt": "terbaik",
    "the best": "terbaik",
    "verivikasi": "verifikasi",
    "no": "nomor",
    "rek": "rekening",
    "mantappp": "mantap",
    "omg": "astaga",
    "ngejawab": "dijawab",
    "ujung2nya": "akhirnya",
    "tf": "transfer",
    "adaaa": "ada",
    "parahhh": "parah",
    "jwb": "jawab",
    "pdahal": "padahal",
    "gk": "tidak"
    }
    #dictionary of stopwords
    stop_factory = StopWordRemoverFactory().get_stop_words() #delete for manual stopword
    stop_factory.pop(17)
    more_stopword = ['ðŸ‘', 'ðŸ˜€', 'ðŸ˜', 'ðŸ˜™ðŸ˜', 'dan', 'yang', 'dari', 'ke', 
                    'sampai', 'ini', 'itu', 'virtual', 'assistant', 'bni', 'syariah', 'call', 
                    'asisten', 'asistent', 'tripa', 'smart', 'aplikasi', 'dokumentasi',
                    'saya', 'anda', 'live', 'chat', 'm-banking', 'm-bankingnya', 'kata', 'telepon', 'sih', 
                    'she', 'seh', 'neh', 'wah', 'astaga', 'customer service', 'cs', 'mah', 'chat', 'bot', 'produk']
    data = stop_factory + more_stopword 
    #delete stop_factory for manual stopword
    dictionary = ArrayDictionary(data)
    #stemmer
    factory = StemmerFactory()
    stemmer = factory. create_stemmer()
    str = StopWordRemover(dictionary)
    #translate to indonesia
    # translator = Translator()
    # translation = translator.translate(review['text'], dest='id')
    #case folding
    text = review.lower()
    #remove punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    #tokenizing
    text = text.split()
    #normalization
    reformed = [appos[word] if word in appos else word for word in text]
    reformed = " ".join(reformed)
    #remove numeric data
    text = re.sub(r"\d+", "", reformed)
    #remove stopwords
    text = str.remove(text)
    #stemming data
    # text = stemmer.stem(text)
    return text

@jwt_required
def printData(tanggal_awal, tanggal_akhir, sentiments, user_id):
    try:
        posts = Posts.query.filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.user_id==user_id).filter(Posts.source_id==2).all()
        Word_Clouds.query.filter(Word_Clouds.user_id==user_id).filter(Word_Clouds.source_id==2).delete(synchronize_session=False)
        db.session.commit()
        data = transform(posts, sentiments)
        temps = []
        for i in range(len(data)):
            for sentiment in sentiments:
                if(data[i]['sentiment'] == int(sentiment)):
                    temps.append(data[i]['post'])
        if(len(temps) > 0):
            ngrams = count_ngrams(temps)
            print_most_frequent(tanggal_awal, tanggal_akhir, ngrams, user_id)
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

@jwt_required
def printAllData(tanggal_awal, tanggal_akhir, sentiments):
    try:
        posts = Posts.query.filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.source_id==2).all()
        data = transform(posts, sentiments)
        temps = []
        for i in range(len(data)):
            for sentiment in sentiments:
                if(data[i]['sentiment'] == int(sentiment)):
                    temps.append(data[i]['post'])
        Word_Clouds.query.filter(Word_Clouds.user_id==1).filter(Word_Clouds.source_id==2).delete(synchronize_session=False)
        db.session.commit()
        if(len(temps) > 0):
            ngrams = count_ngrams(temps)
            print_all_most_frequent(tanggal_awal, tanggal_akhir, ngrams)
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def transform(posts, sentiments):
    array = []
    for i in posts:
        for sentiment in sentiments:
            if(int(sentiment) == i.sentiment):
                array.append(singleTransform(i))
    return array

def singleTransform(posts):
    data = {
        'id' : posts.id,
        'user_name' : posts.username,
        'user_avatar' : posts.user_avatar,
        'post' : posts.post,
        'tanggal_post' : posts.tanggal_post.strftime('%Y-%m-%d'),
        'sumber' : posts.sources.name,
        'aplikasi' : posts.users.nama_aplikasi,
        'link_review' : posts.link_review,
        'rating' : posts.rating,
        'sentiment' : posts.sentiment
    }

    return data

@jwt_required
def show(id):
    try:
        posts = Posts.query.filter_by(id=id).first()
        if not posts:
            return response.badRequest([], 'Empty....')

        data = {
            'id' : posts.id,
            'user_name' : posts.username,
            'user_avatar' : posts.user_avatar,
            'post' : posts.post,
            'tanggal_post' : posts.tanggal_post.strftime('%Y-%m-%d'),
            'sumber' : posts.sources.name,
            'aplikasi' : posts.users.nama_aplikasi,
            'link_review' : posts.link_review,
            'rating' : posts.rating,
            'sentiment' : posts.sentiment
        }
        return response.ok(data, "")
    except Exception as e:
        # print(e)   
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

# @crontab.job(minute="0", hour="1")
def index(tanggal_awal, tanggal_akhir):
    try:
        api = API_Config.query.filter_by(id=4).first()
        api2 = API_Config.query.filter_by(id=5).first()
        users = Users.query.filter_by(is_active=1).all()
        for user in users:
            print(user.app_apps_store)
            if(user.app_apps_store != ''):
                data = []
                sentiment = []
                text = []
                temps = []
                hasil_xml = requests.get(api2.url_api + user.app_apps_store + api2.param1)
                hasil_xml = ET.fromstring(hasil_xml.content)
                # for i in aplikasi:
                hasil = requests.get(api.url_api + user.app_apps_store + api.param1)
                hasil = hasil.json()
                temps = []
                i = 12
                if(hasil['feed']['link'][2]['attributes']['href'] != ''):
                    for j in range(len(hasil['feed']['entry'])):
                        d = datetime.fromisoformat(hasil_xml[i][0].text)
                        tanggal_post = d.strftime('%Y-%m-%d')
                        if(tanggal_post > tanggal_awal and tanggal_post < tanggal_akhir):
                            user_name = hasil['feed']['entry'][j]['author']['name']['label'].encode('ascii', 'ignore')
                            # user_avatar = hasil['results'][j]['userImage']
                            post = hasil['feed']['entry'][j]['content']['label'].encode('ascii', 'ignore')
                            sumber = 2
                            link_review = hasil['feed']['entry'][j]['link']['attributes']['href']
                            rating = hasil['feed']['entry'][j]['im:rating']['label']
                            # sentiment = model_svm(hasil['feed']['entry'][j]['content']['label'])
                            data.append({ "user_name": user_name, "post": post, "tanggal_post": tanggal_post, "sumber": sumber, "user_id": user.id, "link_review": link_review, "rating": rating })
                            text.append(post.decode("utf-8"))
                            temps.append(post.decode("utf-8"))
                            # posts = Posts(user_name=user_name, user_avatar=user_avatar, post=post, tanggal_post=tanggal_post, sumber=sumber,
                            # aplikasi=aplikasi, link_review=link_review, rating=rating, sentiment=sentiment)
                            # db.session.add(posts)
                            # db.session.commit()
                        i = i + 1
                    if(len(data) > 0):
                        sentiments = model_svm(text)
                        sentiments = sentiments.tolist()
                        for i in range(len(data)):
                            user_name = data[i]['user_name']
                            # user_avatar = data[i]['user_avatar']
                            post = data[i]['post']
                            tanggal_post = data[i]['tanggal_post']
                            sumber = data[i]['sumber']
                            user_id = data[i]['user_id']
                            link_review = data[i]['link_review']
                            rating = data[i]['rating']
                            sentiment = sentiments[i]
                            posts = Posts(username=user_name, user_avatar="https://icons-for-free.com/iconfiles/png/512/User+Avatar+Human+Profile+Face-131983793572615800.png", post=post, tanggal_post=tanggal_post, source_id=sumber,
                            user_id=user_id, link_review=link_review, rating=rating, sentiment=sentiment)
                            db.session.add(posts)
                            db.session.commit()
        post_var =  Posts.query.filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.source_id==2).all()
        if len(post_var) > 0:
            return post_var
        else:
            return "Data tidak ada atau kosong"
    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')
        # return response.ok([], "Data kosong")

def tokenize(string):
    return re.findall(r'\w+', string.lower())


def count_ngrams(lines, min_length=1, max_length=1):
    lengths = range(min_length, max_length + 1)
    ngrams = {length: collections.Counter() for length in lengths}
    queue = collections.deque(maxlen=max_length)

    def add_queue():
        current = tuple(queue)
        for length in lengths:
            if len(current) >= length:
                ngrams[length][current[:length]] += 1

    for line in lines:
        for word in tokenize(line):
            queue.append(word)
            if len(queue) >= max_length:
                add_queue()

    while len(queue) > min_length:
        queue.popleft()
        add_queue()

    return ngrams


def print_most_frequent(tanggal_awal, tanggal_akhir, ngrams, user_id, num=10):
    for n in sorted(ngrams):
        for gram, count in ngrams[n].most_common(num):
            word = ' '.join(gram)
            value = count
            search = "%{}%".format(word)
            # SELECT * FROM `post__tests` WHERE post LIKE '%bagus%' AND aplikasi='com.tripa' AND tanggal_post BETWEEN '2020-06-01' AND '2020-06-06'
            # Lanjutkan perihal select max value
            # post_sample = Posts.query.filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.aplikasi==aplikasi).filter(Posts.post.like(search)).all()
            post_sentiment = Posts.query.with_entities(func.avg(Posts.sentiment).label('avg_sentiment')).filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.user_id==user_id).filter(Posts.source_id==2).filter(Posts.post.like(search)).all()
            post_id = Posts.query.filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.user_id==user_id).filter(Posts.source_id==2).filter(Posts.post.like(search)).first()
            sentiment = int(post_sentiment[0].avg_sentiment)
            sample_id = post_id.id
            word_clouds = Word_Clouds(word=word, user_id=user_id, source_id=2, value=value, sentiment=sentiment, sample_id=sample_id)
            db.session.add(word_clouds)
            db.session.commit()

def print_all_most_frequent(tanggal_awal, tanggal_akhir, ngrams, num=10):
    for n in sorted(ngrams):
        for gram, count in ngrams[n].most_common(num):
            word = ' '.join(gram)
            value = count
            search = "%{}%".format(word)
            # SELECT * FROM `post__tests` WHERE post LIKE '%bagus%' AND aplikasi='com.tripa' AND tanggal_post BETWEEN '2020-06-01' AND '2020-06-06'
            # Lanjutkan perihal select max value
            # post_sample = Posts.query.filter(Posts.tanggal_post.between(tanggal_awal, tanggal_akhir)).filter(Posts.aplikasi==aplikasi).filter(Posts.post.like(search)).all()
            post_sentiment = Posts.query.with_entities(func.avg(Posts.sentiment).label('avg_sentiment')).filter(Posts.source_id==2).filter(Posts.post.like(search)).all()
            post_id = Posts.query.filter(Posts.post.like(search)).filter(Posts.source_id==2).first()
            sentiment = int(post_sentiment[0].avg_sentiment)
            sample_id = post_id.id
            word_clouds = Word_Clouds(word=word, user_id=1, source_id=2, value=value, sentiment=sentiment, sample_id=sample_id)
            db.session.add(word_clouds)
            db.session.commit()
