// ================================================================
// TRIMURTI PRODUCT CATALOG — Individual product data
// ================================================================
// 198 unique products across 21 crop groups
// Each hybrid entry has: name, desc, img (individual product image)
// ================================================================

const PRODUCTS = [

  // === Maize (31 products) ===
  {
    id:"maize",
    name:"Maize",
    category:"field-crops",
    type:"Hybrid",
    code:"TMMH",
    active:true,
    order:1,
    detailPage:false,
    description:"• Premium Maize hybrid with very high yield potential • Medium maturity [Rabi: 120-125 days (AP & TS), 140-150 days (BR) & Spring: 95-100 days.] • Long cobs with 16-18 rows & 40-45 seeds / row • Sh...",
    image:"https://trimurti.in/wp-content/uploads/2026/05/Pusa_HQPM-5_3D_pouch_optimized_50.png",
    features:["Premium Maize hybrid with very high yield potential","Long cobs with 16-18 rows & 40-45 seeds / row","Shelling percent: > 80%","Very low cob placement","Yellow orange semi-dent grains with purple shank","Tolerant to heat stress"],
    season:"Kharif / Rabi / Spring",
    duration:"120-125days",
    region:"All India",
    markets:"India",
    special:"Hybrid Maize",
    hybrids:[
      {name:"Pusa HQPM &#8211; 5 Improved",desc:"• Premium Maize hybrid with very high yield potential • Medium maturity [Rabi: 120-125 days (AP & TS), 140-150 days (BR) & Spring: 95-100 days.] • ...",img:"https://trimurti.in/wp-content/uploads/2026/05/Pusa_HQPM-5_3D_pouch_optimized_50.png"},
      {name:"TMMH 8833",desc:"Premium Maize hybrid with very high yield potential Highly suitable for Spring season cultivation being highly heat tolerant (Excellent seed settin...",img:"https://trimurti.in/wp-content/uploads/2026/04/TMMH-8833-3D-Pouch.png"},
      {name:"TMMH 8135",desc:"Maize hybrid with high yield potential Medium maturity and maturity duration in Kharif is 90-95 days, Suitable for high density planting Highly uni...",img:"https://trimurti.in/wp-content/uploads/2025/07/tmmh-8135-3d-pouch_optimized.png"},
      {name:"TMMH 2852",desc:"Premium Maize hybrid with high yield potential Medium maturity (Kharif: 95-100 days & Rabi: 120-125 days) hybrid Erect plant habit, suitable for cl...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2852-3d-pouch_optimized.png"},
      {name:"TMMH 2861",desc:"Premium maize hybrid with very high yield potential Medium maturity: Kharif 90-100 days and Rabi 115-120 days Erect plant habit, suitable for dense...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMMH-2861-3d-POUCH.png"},
      {name:"RAJNATH (TMMH 8863)",desc:"Premium Maize hybrid with very high yield potential Highly suitable for Spring season cultivation being highly heat tolerant (Excellent seed settin...",img:"https://trimurti.in/wp-content/uploads/2025/07/rajnath-tmmh-8863-3d-pouch_optimized.png"},
      {name:"TMMH 8418",desc:"Premium Maize hybrid with very high yield potential Maturity duration: Spring 90-95 days Erect plant type and suitable for high density planting Lo...",img:"https://trimurti.in/wp-content/uploads/2025/07/tmmh-8418-3d-pouch_optimized.png"},
      {name:"SUVEER (TMMH 2882)",desc:"Premium Maize hybrid with very high yield potential Maturity duration: Rabi 140-150 days and Spring 95-100 days) Highly suitable for both Rabi and ...",img:"https://trimurti.in/wp-content/uploads/2025/07/Suveer-TMMH-2882-3d-Pouch.png"},
      {name:"TMMH 8805",desc:"Premium maize hybrid with very high yield potential Medium maturity: Kharif 90-100 days and Rabi 115-120 days Erect plant habit, suitable for close...",img:"https://trimurti.in/wp-content/uploads/2025/07/tmmh-8805-3d-pouch_optimized.png"},
      {name:"TMMH 826.COM",desc:"Premium Maize hybrid suitable for fresh market as GREEN COBS Harvesting for green cobs starts from 75 days for roasting purpose Suitable for high d...",img:"https://trimurti.in/wp-content/uploads/2025/07/tmmh-826_optimized.com-3d-pouch.png"},
      {name:"Trinath TURBO",desc:"Medium maturity maize hybrid Maturity duration – Kharif: 95-100 days & Rabi:130-140 days Erect plant habit, suitable for close space planting Long ...",img:"https://trimurti.in/wp-content/uploads/2024/03/trinath-turbo-tmmh-806-3d-pouch_optimized.png"},
      {name:"TMMH 2855",desc:"• Premium Maize hybrid with very high yield potential • Full season maturity [Rabi: 120-130 days (AP & TG) and 140-150 days (Bihar)] • Suitable for...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2855-3d-pouch_optimized.png"},
      {name:"TMMH 2841",desc:"• Premium Maize hybrid with very high yield potential • Medium maturity [Rabi: 120-125 days (AP & TS), 140-150 days (BR) & Spring: 95-100 days.] • ...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2841-3d-pouch_optimized.png"},
      {name:"TMMH 2834",desc:"• Maize hybrid with high yield potential • Medium maturity (Kharif: 90-100 days) hybrid • Drooping plant habit, suitable for regular space planting...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2834-3d-pouch_optimized.png"},
      {name:"TMMH 2831 Plus",desc:"• Premium Maize hybrid with high yield potential • Medium maturity (Kharif: 95-100 days & Rabi: 120-125 days ) hybrid • Erect plant habit, suitable...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2831-plus-3d-pouch_optimized.png"},
      {name:"TMMH 2831",desc:"Premium Maize hybrid with high-yield potential Medium maturity (Kharif: 95-100 days & Rabi: 120-125 days) hybrid Erect plant habit, suitable for cl...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2831-3d-pouch_optimized.png"},
      {name:"TMMH 801",desc:"• Premium Maize hybrid with high yield potential • Full season maturity [Kharif: 105-110 days, Rabi: 125-130 days & Spring: 100-105] • Erect plant ...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-801-3d-pouch_optimized.png"},
      {name:"Devaraj (TMMH 2845)",desc:"Premium Maize hybrid with very high yield potential Full season maturity [Kharif: 100-105 days, Rabi: 120-130 days (AP & TG) and 140-150 days (Biha...",img:"https://trimurti.in/wp-content/uploads/2023/10/Devraj-TMMH2845-3d-Pouch-1.png"},
      {name:"Darwin (TMMH 2840)",desc:"PIremium Maize hybrid with very high yield potential Full season maturity [Kharif : 100-105 days, Rabi: 120-130 days (AP & TG) and 140-150 days (Bi...",img:"https://trimurti.in/wp-content/uploads/2023/10/darwin-tmmh-2840-3d-pouch_optimized.png"},
      {name:"TMMH 8862",desc:"Maize hybrid with high yield potential Medium maturity – Kharif: 90-95 days Suitable for high-density planting Highly uniform cobs with 14-16 rows ...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-8862-3d-pouch_optimized.png"},
      {name:"TRIVIKRAM  (TMMH 802)",desc:"TRIVIKRAM (TMMH 802) • Maize hybrid with very high yield potential • Full season maturity [Kharif: 110-115 days & Rabi: 140-150 days (Bihar) & 120-...",img:"https://trimurti.in/wp-content/uploads/2023/10/trivikram-tmmh-802_optimized.png"},
      {name:"TMMH 8842",desc:"• Premium Maize hybrid with high yield potential • Medium maturity (Kharif: 90-100 days) hybrid • Semi-erect plant habit • Cobs with 14-16 rows & 4...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-8842-3d-pouch_optimized.png"},
      {name:"TMMH 836",desc:"• Premium Maize hybrid with very high yield potential • Medium maturity and duration is 95-100 days during Kharif season • Very attractive orange s...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-836-3d-pouch_optimized.png"},
      {name:"TMMH 826",desc:"• Premium Maize hybrid with very high yield potential • Full season maturity [Kharif: 105-110 days, Rabi: 120-130 days (AP & TG) and 140-150 days (...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMMH-826-3d-Pouch.png"},
      {name:"TMMH 812",desc:"• Maize hybrid with high yield potential • Early maturity (Kharif :85-90 days and Rabi: 115-125 days) hybrid • Semi-erect plant habit • Cobs with 1...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-812-3d-pouch_optimized.png"},
      {name:"TMMH 807",desc:"• Maize hybrid with high yield potential • Medium maturity – Kharif: 90-95 days, • Suitable for high density planting • Robust and unform cobs with...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-807-3d-pouch_optimized.png"},
      {name:"SUPER TRIVIKRAM (TMMH 844)",desc:"Premium Maize hybrid with very high yield potential Full season maturity [Kharif: 110-115 days, Rabi: 120-130 days (AP & TG) and Spring: 100-105 da...",img:"https://trimurti.in/wp-content/uploads/2023/10/super-trivikram-tmmh-844-3d-pouch_optimized.png"},
      {name:"Srinath (TMMH 804)",desc:"Maize hybrid with high yield potential Early maturity [Kharif: 85-90 days & late Rabi (110-120 days)] hybrid Semi-erect plant habit Cobs with 14-16...",img:"https://trimurti.in/wp-content/uploads/2023/10/srinath-tmmh-804-3d-pouch_optimized.png"},
      {name:"TMMH 824",desc:"Premium Maize hybrid with very high yield potential Medium maturity (Spring: 90-95 days and Rabi: 120-125 days (AP & TS) and 140-150 days (BR) High...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMMH-824-3d-Pouch-1.png"},
      {name:"SAINATH (TMMH 809)",desc:"• Premium Maize hybrid with high yield potential • Medium maturity (Kharif: 90-100 days) hybrid • Semi-erect plant habit • Long cobs with 14-16 row...",img:"https://trimurti.in/wp-content/uploads/2023/10/sainath-tmmh-809-3d-pouch_optimized.png"},
      {name:"Fodder (TMMH2838)",desc:"Maize hybrid with high yield potential Medium maturity; around 90–100 days for Kharif and 115–120 days for Rabi Erect plant structure suitable for ...",img:"https://trimurti.in/wp-content/uploads/2023/10/tmmh-2832-3d-pouch_optimized.png"}
    ]
  },

  // === Rice (56 products) ===
  {
    id:"rice",
    name:"Rice",
    category:"field-crops",
    type:"Hybrid",
    code:"TMR",
    active:true,
    order:2,
    detailPage:false,
    description:"Full season maturing [Kharif: 110-115 days (North & South India) & 115-120 days (East & Central India)] Rice hybrid with very high yield potential Semi-erect plant habit Number of productive tiller...",
    image:"https://trimurti.in/wp-content/uploads/2026/05/Devaki-3D-Pouch-2026-Compressed.png",
    features:["Premium rice","High yield potential","Adapted to diverse conditions"],
    season:"Kharif",
    duration:"110-115days",
    region:"South India",
    markets:"India",
    special:"Hybrid Rice",
    hybrids:[
      {name:"Devaki (JRH &#8211; 5)",desc:"Full season maturing [Kharif: 110-115 days (North & South India) & 115-120 days (East & Central India)] Rice hybrid with very high yield potential ...",img:"https://trimurti.in/wp-content/uploads/2026/05/Devaki-3D-Pouch-2026-Compressed.png"},
      {name:"TMRH 5513 (Nagma)",desc:"Full season maturing [Kharif: 135-135 days (North & South India) & 135-140 days (East & Central India)] Rice hybrid with very high yield potential ...",img:"https://trimurti.in/wp-content/uploads/2026/04/Nagma-Rice-Hybrid.png"},
      {name:"TMRV 1734",desc:"Mid-early maturing rice variety with higher yield potential Maturity duration – Kharif: 120-130 days Semi-erect plant habit Number of productive ti...",img:"https://trimurti.in/wp-content/uploads/2026/04/TMRV-1734-3d-LQ-Pouch.jpg"},
      {name:"PR 126",desc:"Mid – early maturing improved variety with high yield potential Maturity duration: Kharif- 120-125 days and Rabi 130-135 days Semi-erect plant habi...",img:"https://trimurti.in/wp-content/uploads/2026/03/PR126-3D-Pouch-we.png"},
      {name:"TMRH 2135",desc:"Full season maturing [Kharif: 135-135 days (North & South India) & 135-140 days (East & Central India)] Rice hybrid with very high yield potential ...",img:"https://trimurti.in/wp-content/uploads/2026/03/TMRH-2135-3d-Pouch.webp"},
      {name:"DUMDAAR (TMRV 3615)",desc:"Medium maturing Rice variety with high yield potential Maturity duration: Kharif 125-130 days and Rabi 130-135 days Semi-erect plant habit and tole...",img:"https://trimurti.in/wp-content/uploads/2025/07/DUMDAAR-TMRV-3615-NEW-3d-POUCH.png"},
      {name:"BAPPI (TMRV 1686)",desc:"Mid-early maturing rice variety with high yield potential Maturity duration: Kharif – 120-125 days & Rabi – 125-130 days Plant height 100-105 cm wi...",img:"https://trimurti.in/wp-content/uploads/2025/07/BAPPI-1686-NEW-3d-POUCH.png"},
      {name:"SNIGDHA (TMRV 1685)",desc:"Medium maturing rice variety with high yield potential Maturity duration: Kharif – 130-135 days Plant height 100-105 cm with semi-dwarf plant habit...",img:"https://trimurti.in/wp-content/uploads/2025/07/SNIGDHA-1685-NEW-3d-POUCH-1.png"},
      {name:"TMRV 1682",desc:"Medium maturing [Kharif: 130-135 days] improved rice variety with very high yield potential Semi-erect plant habit Number of productive tillers: 12...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMMV-1682-NEW-3d-POUCH-1.png"},
      {name:"TRIMURTI 92 (TMRV 92)",desc:"Mid-early maturing (115-120 days) basmati rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 10-12 Semi-dw...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMRV-92-3d-POUCH.png"},
      {name:"USTAAD (TMRV 1621)",desc:"Medium maturing [Kharif: 125-135 days and Rabi: 130-140 days] improved rice variety with high yield potential Semi-erect plant habit Number of prod...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMRV-1621-USTAAD-3d-POUCH.png"},
      {name:"BADRINATH (TMRV 1666)",desc:"Mid-early maturing rice variety with higher yield potential Maturity duration – Kharif: 120-125 days and Rabi: 125-130 days Semi-erect plant habit ...",img:"https://trimurti.in/wp-content/uploads/2025/07/BADRINATH-3d-POUCH-1-scaled.png"},
      {name:"SHAN-E-DAWAT PLUS (TMRV 1509)",desc:"Early maturing (Kharif:115-120 days) Basmati Rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 8-10 Semi-...",img:"https://trimurti.in/wp-content/uploads/2025/07/Shaan-E-Dawat-plus-NEW-Pouch.png"},
      {name:"SHAN-E-DAWAT (TMRV 1121)",desc:"Mid-early maturing (125-135 days) basmati rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 8-10 Semi-dwa...",img:"https://trimurti.in/wp-content/uploads/2025/07/Shaan-E-Dawat-NEW-Pouch.png"},
      {name:"TMRH 2156",desc:"Mid-early maturing [Kharif: 115-120 days & Rabi: 120-125 days] very high yielding rice hybrid Semi-erect plant habit Number of productive tillers: ...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMRH_2156_web_-HR-min.png"},
      {name:"SHER-E-BASMATI (TMRH 1105)",desc:"Mid-early maturing (Kharif: 110-115 days) Basmati hybrid rice with higher yield potential Semi-erect plant habit Number of productive tillers: 12-1...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMRH_1105_Web_-HR-min.webp"},
      {name:"TMRH 5559",desc:"Full season maturing [Kharif: 135-135 days (North & South India) & 135-140 days (East & Central India)] Rice hybrid with very high yield potential ...",img:"https://trimurti.in/wp-content/uploads/2025/07/WhatsApp-Image-2026-03-31-at-21.42.19.jpeg"},
      {name:"TMRH 5535",desc:"Mid-early maturing [Kharif: 120-125 days & Rabi: 125-130 days] very high yielding hybrid rice Semi-erect plant habit Number of productive tillers: ...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMRH_5535_web_-HR-min.png"},
      {name:"TMRH 5788",desc:"Mid-early maturing (Kharif: 116-122 days) hybrid rice with higher yield potential Semi-erect plant habit Number of productive tillers: 12-15 Semi-d...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMRH_5788_web_-HR-min.png"},
      {name:"TMRV 1626 (Yamini)",desc:"Medium maturing (Kharif:125-130 days) improved rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 10-15 Se...",img:"https://trimurti.in/wp-content/uploads/2024/03/TMRV-1626-Yamini-e1776840245244.jpeg"},
      {name:"TMRH 2184",desc:"TMRH2184 • Early maturing [Kharif: 110-115 days] Rice hybrid with high yield potential • Semi-erect plant habit • Number of productive tillers: 12-...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_2184_web_-HR-min.png"},
      {name:"TMRH 2161",desc:"• Medium maturing [Kharif: 115-125 days and Rabi: 125-135 days] Rice hybrid with high yield potential • Semi-erect plant habit having 100-110 cm pl...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_2161_web_-HR-min.png"},
      {name:"TMRH 2151",desc:"• Full season maturing [Kharif: 135 -145 days] rice hybrid with high yield potential • Semi-erect plant habit • Number of productive tillers: 14-16...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_2151_web_-HR-min.png"},
      {name:"TMRH 2106",desc:"• Full seasong maturing [Kharif: 130-135 days (North & South India) 135-140 days (East & Central India)] hybrid with high yield potential • Semi-er...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_2106_web_-HR-min.png"},
      {name:"Shivi Fast",desc:"SHIVI FAST (TMRH 2110) • Early maturing [Kharif: 105-110 days (North & South India) & 110-115 (East & Central India)] hybrid with high yield potent...",img:"https://trimurti.in/wp-content/uploads/2023/10/Shivi_Fast_Web_-HR-min.webp"},
      {name:"Sarna (TMRH 111)",desc:"SARNA (TMRH 111) • Medium maturing [Kharif: 115-120 days (North & South India) & 120-125 days (East & Central India) and Rabi: 125-130 days] Rice h...",img:"https://trimurti.in/wp-content/uploads/2023/10/Sarna_web_-HR-min.png"},
      {name:"Chetak (TMRH 2171)",desc:"CHETAK (TMRH 2171) • Early maturing (Kharif: 112-117 days) Basmati Rice hybrid yield potential • Semi-erect plant habit • Number of productive till...",img:"https://trimurti.in/wp-content/uploads/2023/10/Chetak_web_-HR-min.png"},
      {name:"Chetak Gold (TMRH 2112)",desc:"CHETAK GOLD (TMRH 2112) • Mid-early maturing (Kharif: 118-125 days) hybrid basmati rice with high yield potential • Semi-erect plant habit • Number...",img:"https://trimurti.in/wp-content/uploads/2023/10/Chetak_Gold_Web_-HR-min.png"},
      {name:"TMRH 5786",desc:"Salient Features of TMRH 5786 Maturity: Mid-early maturity (Kharif: 120-125 days & Rabi; 125-130 days) Plant Type & Morphology: Medium-tall plants ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_5786_web_-HR-min.png"},
      {name:"TMRH 5750",desc:"• Mid-early maturing [Kharif: 115-120 days (North & South India) & 120-125 days (East & Central India) & Rabi: 125-130 days] • Semi-erect plant hab...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_5750_web_-HR-min.png"},
      {name:"TMRH 5556",desc:"• Medium maturing [Kharif: 125-130 days (North & South India) & 135-140 days (East & Central India)] Rice hybrid with very high yield potential • S...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_5556_web_-HR-min.png"},
      {name:"TMRH 5544",desc:"• Medium maturing (Kharif: 115-120 days & Rabi: 125-135 days) hybrid with very high yield potential • Semi-erect plant habit • Number of productive...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_5544_web_-HR-min.png"},
      {name:"TMRH 129",desc:"• Early maturing [Kharif: 108-112 days (North India) & 115-120 days (East & Central India)] Rice hybrid • Semi-erect plant habit • Number of produc...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_129_web_-HR-min.png"},
      {name:"TMRH 101",desc:"• Early maturing [Kharif: 101-108 days & Rabi: 130-135 days] hybrid with high yield potential • Semi-erect plant habit • Number of productive tille...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH_101_web_-HR-min.png"},
      {name:"Supriya (TMRH 174)",desc:"• Full season maturing (Kharif: 132-138 days & Rabi: 140-145 days) Rice hybrid with very high yield potential • Semi-erect plant habit • Number of ...",img:"https://trimurti.in/wp-content/uploads/2023/10/Supriya_Web_-HR-min.webp"},
      {name:"PAVITRA (TMRH 108)",desc:"• Early maturing (Kharif: 115-120 days) Basmati Rice hybrid with high yield potential • Semi-erect plant habit • Number of productive tillers: 12-1...",img:"https://trimurti.in/wp-content/uploads/2023/10/Pavitra_web_-HR-min.png"},
      {name:"MANI (TMRH 114)",desc:"Full season maturing [Kharif: 135-140 days & Rabi: 145-150 days] Rice hybrid with very high yield potential Semi-erect plant habit Number of produc...",img:"https://trimurti.in/wp-content/uploads/2023/10/Mani_web_-HR-min.png"},
      {name:"Kamakshi (TMRH 102)",desc:"Medium maturing Rice hybrid [Kharif: 115-120 days (North & South India) & 120-125 days (East & Central India) & Rabi: 125-130 days ] Semi-erect pla...",img:"https://trimurti.in/wp-content/uploads/2023/10/Kamakshi_web_-HR-min.png"},
      {name:"GULABOO (TMRH 106)",desc:"• Mid-early maturing (Kharif: 116-122 days) basmati rice hybrid with higher yield potential • Semi-erect plant habit • Number of productive tillers...",img:"https://trimurti.in/wp-content/uploads/2023/10/Gulaboo_web_-HR-min.png"},
      {name:"DEVI (TMRH 107)",desc:"•Medium maturing (Kharif: 125-130 days & Rabi: 130-135 days) hybrid with high yield potential • Number of productive tillers: 12-14 • Semi-dwarf pl...",img:"https://trimurti.in/wp-content/uploads/2023/10/Devi_web_-HR-min.webp"},
      {name:"TMRV 3649",desc:"• Mid – Early maturing [Kharif: 115-120 days & Rabi 120-125 days] Rice variety with high yield potential • Semi-erect plant habit having 100 – 110 ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-3649-PNG.png"},
      {name:"TMRV 3641",desc:"Medium maturing [Kharif: 125-130 days and Rabi: 130-135 days] Rice variety with high yield potential • Semi-erect plant habit • Number of productiv...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-3641-3D-PNG.png"},
      {name:"TMRV 3644",desc:"Full Season maturing (Kharif: 140-145 days & Rabi: 145-155 days) variety with high yield potential • Semi-erect plant habit • Number of productive ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRH-3644-3D-POUCH.png"},
      {name:"TM 09",desc:"• Early maturing [Kharif: 115-120 days] Basmati Rice variety with high yield potential • Semi-erect plant habit • Number of productive tillers: 10-...",img:"https://trimurti.in/wp-content/uploads/2023/10/TM-09-PNG-_.png"},
      {name:"Slym",desc:"SLYM (TMRV 3618) • Medium maturing [Kharif: 125 -130 days & Rabi: 130-135 day Rice variety with high yield potential • Semi-erect plant habit havin...",img:"https://trimurti.in/wp-content/uploads/2023/10/Slym_3D-PNG.png"},
      {name:"PB 1692",desc:"• Early maturing (Kharif: 115-120 days) Basmati Rice variety with high yield potential • Semi-erect plant habit • Number of productive tillers: 10-...",img:"https://trimurti.in/wp-content/uploads/2023/10/PB-scaled.webp"},
      {name:"TMRV 1629",desc:"• Full Season maturing (Kharif: 150-155 days & Rabi: 155-160 days) Rice variety with high yield potential • Semi-erect plant habit • Number of prod...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-1629_3D-PNG.png"},
      {name:"TMRV 1628",desc:"• Mid-early maturing (Kharif: 120-125 days) Rice variety with high yield potential • Semi-erect plant habit • Number of productive tillers: 10-12 •...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-1628-PNG_.png"},
      {name:"TMRV 1617",desc:"• Early maturing [Kharif: 100-105 days] rice variety with high yield potential • Semi-erect plant habit • Number of productive tillers: 10-12 • Sem...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-1617-PNG.png"},
      {name:"TMRV 1609",desc:"• Full Season maturing (Kharif: 150-155 days & Rabi: 142-148 days) Rice variety with high yield potential • Semi-erect plant habit • Number of prod...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-1609-PNG.png"},
      {name:"TMRV 1611",desc:"• Full Season maturing (Kharif: 140-145 days & Rabi: 145-155 days) Rice variety with high yield potential • Semi-erect plant habit • Number of prod...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-PNG-1611_.png"},
      {name:"VISHWANATH (TMRV 1610)",desc:"Mid-early maturing (Kharif: 115-120 days) Rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 12-14 Semi-dw...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMRV-1610-VISHWANATH-PNG.png"},
      {name:"Tinku",desc:"• Medium maturing (Kharif: 130-135 days and Rabi: 135-140 days) rice variety with high yield potential • Semi-erect plant habit • Number of product...",img:"https://trimurti.in/wp-content/uploads/2023/10/Tinku_-PNG.png"},
      {name:"Shurma (TMRV 1632)",desc:"Medium maturing [Kharif: 125-130 days & Rabi:130-135 days] Rice variety with high yield potential Semi-erect plant habit Number of productive tille...",img:"https://trimurti.in/wp-content/uploads/2023/10/Surma_3D-Pouch-PNG.png"},
      {name:"Shaan-e-dawat plus (1509)",desc:"Shaan-e-dawat plus (1509) •Early maturing (Kharif: 115-120 days) Basmati Rice variety with high yield potential • Semi-erect plant habit • Number o...",img:"https://trimurti.in/wp-content/uploads/2023/10/Shaan-e-dawat-plus-PNG.png"},
      {name:"PB 1718",desc:"Medium maturing (Kharif: 13 5-140 days) Basmati Rice variety with high yield potential • Semi-erect plant habit • Number of productive tillers: 10-...",img:"https://trimurti.in/wp-content/uploads/2023/10/1718-3D-POUCH.png"}
    ]
  },

  // === Mustard (13 products) ===
  {
    id:"mustard",
    name:"Mustard",
    category:"field-crops",
    type:"Hybrid",
    code:"TM",
    active:true,
    order:3,
    detailPage:false,
    description:"Improved Mustard Variety with very high yield potential medium maturity: 122-128 days Plant height: 160-170 cm Main shoot length: 65-75 cm High numbers of primary and secondary branches Bold seeded...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/Kaalia-Gold-Mustard.png",
    features:["Yellow Mustard variety with high yield potential","Medium maturity: 115-120 days","Plant height: 140-150 cm","Main shoot length: 50-60 cm","More number of primary and secondary branches","Yellow coloured bold grains having 14-16 grains / silique"],
    season:"Rabi",
    duration:"122-128days",
    region:"All India",
    markets:"India",
    special:"Mustard Variety",
    hybrids:[
      {name:"KAALIA GOLD (TMMD 9242)",desc:"Improved Mustard Variety with very high yield potential medium maturity: 122-128 days Plant height: 160-170 cm Main shoot length: 65-75 cm High num...",img:"https://trimurti.in/wp-content/uploads/2025/07/Kaalia-Gold-Mustard.png"},
      {name:"TMMD 2905",desc:"Medium maturing (122-130 days) Mustard variety with very high yield potential Erect plant with tall plant height (160-180 cm) Number of primary bra...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMMD-2905.png"},
      {name:"TMMD 2904",desc:"• Yellow Mustard variety with high yield potential • Medium maturity: 115-120 days • Plant height: 140-150 cm • Main shoot length: 50-60 cm • More ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMMD-2904.png"},
      {name:"TMMD 2901",desc:"• Medium maturing (118-122 days) Mustard variety with high yield potential • Erect plant with tall plant height (150-170 cm) • Number of primary br...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMMD-2901-PNG.png"},
      {name:"TM 9988",desc:"",img:"https://trimurti.in/wp-content/uploads/2023/10/TM_9988_-HR-min.webp"},
      {name:"TM 917",desc:"Mustard hybrid with very high yield potential Good performance under cold temperatures • Maturity: 120-125 days • Plant height: 150-165 cm • Main s...",img:"https://trimurti.in/wp-content/uploads/2023/10/TM_917_-HR-min.webp"},
      {name:"Dhumdaar",desc:"Medium maturing (122-130 days) Mustard variety with very high yield potential Erect plant with tall plant height (160-180 cm) Number of primary bra...",img:"https://trimurti.in/wp-content/uploads/2023/10/Dumdaar-PNG.png"},
      {name:"Ustaad (TM 914)",desc:"USTAAD (TM 914) • Mustard hybrid with very high yield potential • Maturity: 120-130 days • Plant height: 160-175 cm • Main shoot length: 65-75 cm •...",img:"https://trimurti.in/wp-content/uploads/2023/10/ustaad_web_-HR-min.webp"},
      {name:"TM 936",desc:"Mustard hybrid with very high yield potential Maturity: 125-130 days Plant height: 160-180 cm Main shoot length: 60-75 cm Branching starts from the...",img:"https://trimurti.in/wp-content/uploads/2023/10/TM_936_-HR-min.webp"},
      {name:"Kashinath (TMMD 91)",desc:"KASHINATH (TMMD 91) • Mustard variety with high yield potential • Medium maturity: 115-125 days • Plant height: 150-170 cm • Main shoot length: 60-...",img:"https://trimurti.in/wp-content/uploads/2023/10/Kashinath.png"},
      {name:"Kaalia (TMMD 92)",desc:"KAALIA (TMMD 92) • Mustard variety with very high yield potential • Medium maturity: 125-135 days • Plant height: 170-180 cm • Main shoot length: 7...",img:"https://trimurti.in/wp-content/uploads/2023/10/Kaalia.png"},
      {name:"Julie (TMMD 97)",desc:"JULIE (TMMD 97) • Yellow Mustard variety • Early maturity: 98-104 days • Plant height: 110-120 cm • Main shoot length :50-60 cm • Bold seed and 10-...",img:"https://trimurti.in/wp-content/uploads/2023/10/Julie_.png"},
      {name:"Ghungroo (TMMD 99)",desc:"GHUNGROO (TMMD 99) • Yellow Mustard variety • Medium maturity: 100-110 days • Plant height: 115-120 cm • Main shoot length: 55-65 cm • Bold seed an...",img:"https://trimurti.in/wp-content/uploads/2023/10/GHUNGROO-TMMD-99.png"}
    ]
  },

  // === Bajra (Pearl Millet) (5 products) ===
  {
    id:"bajra",
    name:"Bajra (Pearl Millet)",
    category:"field-crops",
    type:"Hybrid",
    code:"TMBH",
    active:true,
    order:4,
    detailPage:false,
    description:"• Early to medium maturing (Kharif: 78-82 days) hybrid with very high yield potential •Erect plant with tall plant height (230-250 cm) •Number of productive tillers: 4-6 •Panicle: 28-32 cm long, ca...",
    image:"https://trimurti.in/wp-content/uploads/2026/04/TMBH-601-Optium.png",
    features:["Erect plant with tall plant height (230-250 cm)","Number of productive tillers: 4-6","Panicle: 28-32 cm long, candle type and compact panicle with good girth","Deep grey bold grains","Excellent stay green fodder with very high stover yield","Resistant to downy mildew and major pests"],
    season:"Kharif / Summer",
    duration:"78-82days",
    region:"All India",
    markets:"India",
    special:"Hybrid Bajra",
    hybrids:[
      {name:"TMBH 601",desc:"• Early to medium maturing (Kharif: 78-82 days) hybrid with very high yield potential •Erect plant with tall plant height (230-250 cm) •Number of p...",img:"https://trimurti.in/wp-content/uploads/2026/04/TMBH-601-Optium.png"},
      {name:"TMBH 602",desc:"• Early to medium maturing (Kharif: 78-82 days) hybrid with very high yield potential •Erect plant with tall plant height (230-250 cm) •Number of p...",img:"https://trimurti.in/wp-content/uploads/2025/12/TMBH_602_-HR-min.webp"},
      {name:"TMBH 2627",desc:"Early maturing (Kharif: 75-80 days) hybrid with high yield potential Erect plant with plant height 210-230 cm Number of productive tillers: 5-8 Lon...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMBH_2627_-HR-min.webp"},
      {name:"Vitagraze (TMFH 1251)",desc:"VITAGRAZE (TaTh 1251) • Multi-cut forage bajra hybrid with high yield potential • Harvesting starts very early as there is no HCN content in this f...",img:"https://trimurti.in/wp-content/uploads/2023/10/vitagraze-3d-pouch.png"},
      {name:"TMFH 1255",desc:"Multi-cut forage bajra hybrid with high yield potential Harvesting starts very early as there is no HCN content in this fodder Good quality fodder ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMFH-1255-PNG-.png"}
    ]
  },

  // === Jowar (Sorghum) (3 products) ===
  {
    id:"jowar",
    name:"Jowar (Sorghum)",
    category:"field-crops",
    type:"Hybrid",
    code:"TMFH",
    active:true,
    order:5,
    detailPage:false,
    description:"Single cut forage Sorghum hybrid for direct feeding and Silage Very tall height with Late flowering (>85 days) Thick, juicy sweet stem with soft internodes Higher green fodder yield with good nutri...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/TOP-DAIRY-NEW-_3D-Pouch.png",
    features:["Single cut Sweet Sorghum fodder but can be taken another cut","Juicy stems with sweetness and preferred by cattle","Plant height: 280 – 320 cm","Good for silage making","Higher Brix and higher in protein","Higher digestibility and platability"],
    season:"Kharif / Spring",
    region:"All India",
    markets:"India",
    special:"Fodder",
    hybrids:[
      {name:"TOP DAIRY (TMFH 1275)",desc:"Single cut forage Sorghum hybrid for direct feeding and Silage Very tall height with Late flowering (>85 days) Thick, juicy sweet stem with soft in...",img:"https://trimurti.in/wp-content/uploads/2025/07/TOP-DAIRY-NEW-_3D-Pouch.png"},
      {name:"DAIRY DON (TMFH 1222)",desc:"Multi-cut Forage Sorghum hybrid with high yield potential Fast growth with excellent regrowth Thick, soft juicy, semi-sweet stem and having high di...",img:"https://trimurti.in/wp-content/uploads/2025/07/DAIRY-DON-_3D-Pouch.png"},
      {name:"Sweet Fora (TMFH 1276)",desc:"SWEET FORA (TMFH 1276) • Single cut Sweet Sorghum fodder but can be taken another cut • Juicy stems with sweetness and preferred by cattle • Plant ...",img:"https://trimurti.in/wp-content/uploads/2023/10/SWEET-FORA-3DE-pouch.png"}
    ]
  },

  // === Sunflower (1 products) ===
  {
    id:"sunflower",
    name:"Sunflower",
    category:"field-crops",
    type:"Hybrid",
    code:"TMSF",
    active:true,
    order:6,
    detailPage:false,
    description:"JEWEL (TV1SH 1701) • Sunflower hybrid suitable for both medium and light soils • High yield potential • Maturity duration: 110-120 days • Plant semi-droopy type and height is 100-110 cm • Head is f...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/Jewel.png",
    features:["Sunflower hybrid suitable for both medium and light soils","High yield potential","Maturity duration: 110-120 days","Plant semi-droopy type and height is 100-110 cm","Head is flat to convex, very compact and uniform seed setting up to centre","Higher oil percent (42-44 %)"],
    duration:"110-120days",
    region:"All India",
    markets:"India",
    special:"Hybrid Sunflower",
    hybrids:[
      {name:"Jewel (TMSF 1701)",desc:"JEWEL (TV1SH 1701) • Sunflower hybrid suitable for both medium and light soils • High yield potential • Maturity duration: 110-120 days • Plant sem...",img:"https://trimurti.in/wp-content/uploads/2023/10/Jewel.png"}
    ]
  },

  // === Wheat (2 products) ===
  {
    id:"wheat",
    name:"Wheat",
    category:"field-crops",
    type:"Variety",
    code:"TMW",
    active:true,
    order:7,
    detailPage:false,
    description:"• Very high yielding Wheat variety • Days to 50 % spike emergence: 95-105 days • Maturity duration: 130-140 days • Average Plant Height: 85-95 cm • No. of productive tillers: 15-20 • Very attractiv...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/TMW-3838.png",
    features:["Very high yielding Wheat variety","Days to 50 % spike emergence: 95-105 days","Maturity duration: 130-140 days","Average Plant Height: 85-95 cm","No. of productive tillers: 15-20","Very attractive bold lustrous grains"],
    duration:"95-105days",
    region:"All India",
    markets:"India",
    special:"Wheat Variety",
    hybrids:[
      {name:"TMW 3838",desc:"• Very high yielding Wheat variety • Days to 50 % spike emergence: 95-105 days • Maturity duration: 130-140 days • Average Plant Height: 85-95 cm •...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMW-3838.png"},
      {name:"Lokpriya (TMW 3888)",desc:"LOKPRIYA (TMW 3888) • Wheat variety with very high yield potential • Semi-erect plant type • Days to 50 % spike emergence: 90-100 days • Maturity d...",img:"https://trimurti.in/wp-content/uploads/2023/10/Lokpriya.png"}
    ]
  },

  // === Nepal Products (5 products) ===
  {
    id:"nepal",
    name:"Nepal Products",
    category:"field-crops",
    type:"Hybrid",
    code:"TMR",
    active:true,
    order:8,
    detailPage:false,
    description:"Medium maturing (Kharif:125-130 days) improved rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 10-15 Semi-dwarf plant type having 95 -105 cm plant height...",
    image:"https://trimurti.in/wp-content/uploads/2025/11/TMRV-1626-3d-Pouch.png",
    features:["Maize hybrid with high yield potential","Medium maturity (Kharif: 90 – 100 days) hybrid","Semi-erect plant habit","Cobs with 14-16 rows","Number of grains I row: 35-40","Attractive orange semi-flint grains"],
    season:"Kharif",
    duration:"125-130days",
    region:"Nepal",
    markets:"India, Nepal",
    hybrids:[
      {name:"TMRV 1626",desc:"Medium maturing (Kharif:125-130 days) improved rice variety with high yield potential Semi-erect plant habit Number of productive tillers: 10-15 Se...",img:"https://trimurti.in/wp-content/uploads/2025/11/TMRV-1626-3d-Pouch.png"},
      {name:"TMMH 846",desc:"• Maize hybrid with high yield potential • Medium maturity (Kharif: 90 – 100 days) hybrid • Semi-erect plant habit • Cobs with 14-16 rows • Number ...",img:"https://trimurti.in/wp-content/uploads/2025/11/TMMH-846-NEPALI-3d-POUCH-scaled.png"},
      {name:"Trinath (TMMH 806)",desc:"",img:"https://trimurti.in/wp-content/uploads/2025/11/Untitled-1.png"},
      {name:"TMMH 2858",desc:"• Premium Maize hybrid with very high yield potential • Full season maturity [Rabi: 120-130 days] • Suitable for high density planting • Long cobs ...",img:"https://trimurti.in/wp-content/uploads/2025/11/TMMH-2858.png"},
      {name:"TMRH 124",desc:"• Medium maturing (Kharif: 120-125 days) hybrid with high yield potential • Semi-erect plant habit • Number of productive tillers: 12-15 • Semi-dwa...",img:"https://trimurti.in/wp-content/uploads/2024/03/nepal-124.webp"}
    ]
  },

  // === Tomato (12 products) ===
  {
    id:"tomato",
    name:"Tomato",
    category:"vegetables",
    type:"Hybrid",
    code:"TMTH",
    active:true,
    order:9,
    detailPage:false,
    description:"• Tomato hybrid for fresh market with very high yield potential • Semi-determinate plant type • Picking starts from 60-65 days after transplanting • Flat round fruit and average weight: 90-100 g • ...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-2267_.png",
    features:["Tomato hybrid for fresh market with very high yield potential","Semi-determinate plant type","Picking starts from 60-65 days after transplanting","Flat round fruit and average weight: 90-100 g","Fruits are firm with good shelf life","Tolerant to Tomato virus (TyLCV) & other major diseases"],
    season:"Kharif / Rabi / Summer",
    duration:"60-65days",
    region:"All India",
    markets:"India",
    special:"Tomato",
    hybrids:[
      {name:"TMTH 2267",desc:"• Tomato hybrid for fresh market with very high yield potential • Semi-determinate plant type • Picking starts from 60-65 days after transplanting ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-2267_.png"},
      {name:"TMTH 2230",desc:"• Tomato hybrid for fresh market and processing purpose with very high yield potential • Semi-determinate plant type • Picking starts from 70-75 da...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-2230_.png"},
      {name:"TMTH 2226",desc:"* Hybrid for fresh market with high yield potential • Recommended for both Kharif and Rabi seasons • Picking starts from 50-55 days after transplan...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-2226.png"},
      {name:"TMTH 215",desc:"• Hybrid for fresh market with high yield potential • Recommended for Kharif, Rabi and Summer seasons • Semi-determinate plant type • Picking start...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-215_.png"},
      {name:"TMTH 288",desc:"TMTH 228 • Tomato hybrid for fresh market with high yield potential • Very widely adapted for cultivation for Kharif, Rabi and Summer seasons • Pic...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-288.png"},
      {name:"TMTH 255",desc:"• Tomato hybrid for fresh market with high yield potential • Recommended for year-round cultivation during Kharif, Rabi & Summer seasons • Picking ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-255.png"},
      {name:"TMTH 231",desc:"• Tomato hybrid for fresh market purpose with very high yield potential • Picking starts from 60-65 days after transplanting • Semi-determinate pla...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMTH-231.png"},
      {name:"Rype (TMTH 205)",desc:"RYPE (TMTH 205) • Hybrid for fresh market with high yield potential • Recommended for cultivation during Kharif, Rabi & Summer seasons • Picking st...",img:"https://trimurti.in/wp-content/uploads/2023/10/RYPE.png"},
      {name:"Holi",desc:"HOLI (TMTH206) • Tomato hybrid for fresh market purpose with high yield potential • Picking starts from 50-55 days after transplanting • Determinat...",img:"https://trimurti.in/wp-content/uploads/2023/10/Holi_.png"},
      {name:"Diya (TMTH 208)",desc:"DIYA (TMTH 208) • Indeterminate type tomato hybrid with very high yield potential • Picking starts from 60-65 days after transplanting • Round firm...",img:"https://trimurti.in/wp-content/uploads/2023/10/Diya_.png"},
      {name:"Chamki",desc:"CHAMKI (TMTH 209) • Tomato hybrid for fresh market with high yield potential • Picking starts from 50-55 days after transplanting • Semi-determinat...",img:"https://trimurti.in/wp-content/uploads/2023/10/CHAMKI.png"},
      {name:"Abeesh (TMTH 222)",desc:"ABEESH (TMTH^22) • Tomato hybrid for fresh market and processing with very high yield potential • Picking starts from 70-75 days after transplantin...",img:"https://trimurti.in/wp-content/uploads/2023/10/Abeesh_.png"}
    ]
  },

  // === Chilli (17 products) ===
  {
    id:"chilli",
    name:"Chilli",
    category:"vegetables",
    type:"Hybrid",
    code:"TMPH",
    active:true,
    order:10,
    detailPage:false,
    description:"• Green Chilli hybrid with very high yield potential • Picking starts for green chilli after 65-70 days from transplanting • Semi-Erect plant type • Fruit length : 8-9 cm • Immature fruit is dark g...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-2446_.png",
    features:["Green Chilli hybrid with very high yield potential","Picking starts for green chilli after 65-70 days from transplanting","Semi-Erect plant type","Fruit length : 8-9 cm","Immature fruit is dark green, shiny and very attractive in colour","Profuse fruiting and more fruits per picking"],
    season:"Summer",
    duration:"65-70days",
    region:"All India",
    markets:"India",
    special:"Chilli",
    hybrids:[
      {name:"TMPH 2446",desc:"• Green Chilli hybrid with very high yield potential • Picking starts for green chilli after 65-70 days from transplanting • Semi-Erect plant type ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-2446_.png"},
      {name:"TMPH 2441",desc:"• Green chili hybrid with very high yield potential • Picking starts for green chilli after 60-65 days from transplanting • Erect with tall plant t...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-2441_.png"},
      {name:"TMPH 463",desc:"• Dual purpose chilli hybrid (i.e. as green & dry chilli) • Picking starts for green chilli after 65-70 days & for dry chilli after 105-110 days fr...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-463.png"},
      {name:"TMPH 403 (SIVARANJANI)",desc:"TMPH 403 (SIVARANJANI) • Dry Chilli hybrid with very high color value • Picking starts for dry chilli after 102-108 days from transplanting • Erect...",img:"https://trimurti.in/wp-content/uploads/2023/10/SIVARANJANI.png"},
      {name:"LEONE (TMPH 434)",desc:"Dual purpose chilli hybrid (i.e. as green & dry chilli) Picking starts for green chilli after 70-75 days & for dry chilli after 115-120 days from t...",img:"https://trimurti.in/wp-content/uploads/2023/10/LE.ONE_.png"},
      {name:"TMPH 489",desc:"• Dual purpose chilli hybrid (i.e. as green & dry chilli) • Picking starts for green chilli after 70-75 days & for dry chilli after 115-120 days fr...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-489.png"},
      {name:"TMPH 449",desc:"• Green Chilli Hybrid with high yield potential • Picking starts for green chilli after 65-70 days from transplanting • Semi-Erect with tall plant ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-449.png"},
      {name:"TMPH 444",desc:"• Dual purpose chilli hybrid (i.e. as green & dry chilli) • Picking starts for green chilli after 70-75 days & for dry chilli after 110-115 days fr...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-444.png"},
      {name:"TMPH 443",desc:"• Green Chilli Hybrid with very high yield potential • Picking starts for green chilli after 60-65 days from transplanting • Heat tolerant and suit...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-443_.png"},
      {name:"TMPH 439",desc:"• Hybrid ideal as green chilli • Picking starts for green chilli after 70-75 days from transplanting • Semi-Erect with tall plant type with cluster...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-439.png"},
      {name:"TMPH 411",desc:"• Dry Chilli hybrid with very high color value • Picking starts for dry chilli after 100-105 days from transplanting • Erect with tall plant type •...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMPH-411.png"},
      {name:"Raima + (TMPH 417)",desc:"RAIMA + • Green Chilli hybrid with high yield potential • Picking starts for green chilli after 65-70 days from transplanting • Erect with tall pla...",img:"https://trimurti.in/wp-content/uploads/2023/10/RAIMA-PLUS.png"},
      {name:"Purvi (TMPH 406)",desc:"PURVI (TMPH 406) • Dry Chilli hybrid • Picking starts for dry chilli after l lO-l 15 days from transplanting • Erect with tall plant type • Fruit l...",img:"https://trimurti.in/wp-content/uploads/2023/10/purvi.png"},
      {name:"Nagma (TMPH 404)",desc:"NAGMA (TMPH 404) • Dual purpose chilli hybrid (i.e. as green & dry chilli) • Picking starts for green chilli after 70-75 days & for dry chilli afte...",img:"https://trimurti.in/wp-content/uploads/2023/10/NAGMA.png"},
      {name:"Klik (TMPH 401)",desc:"KLIK (TMPH 401) • Green Chilli hybrid • Picking starts for green chilli after 65-70 days from transplanting • High yield potential • Semi-Erect pla...",img:"https://trimurti.in/wp-content/uploads/2023/10/klik-pouch.png"},
      {name:"Jhalak (TMPH 424)",desc:"JHALAK (TMPH 424) • Green Chilli hybrid with very high yield potential • Picking starts for green chilli after 55-60 days from transplanting • Semi...",img:"https://trimurti.in/wp-content/uploads/2023/10/Jhalak_3d.png"},
      {name:"Aparna (TMPH 408)",desc:"",img:"https://trimurti.in/wp-content/uploads/2023/10/Aparna.png"}
    ]
  },

  // === Okra (Lady Finger) (14 products) ===
  {
    id:"okra",
    name:"Okra (Lady Finger)",
    category:"vegetables",
    type:"Hybrid",
    code:"TMOH",
    active:true,
    order:11,
    detailPage:false,
    description:"Okra Hybrid with very high yield potential Picking starts from 45-48 days after sowing Erect with tall plant type Dark green shiny fruits having 12-14 cm length at picking Resistant to Yellow Vein ...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/TMOH-333_3D-Pouch.png",
    features:["Tolerant to Yellow Vein Mosaic Virus (YVMV)","Picking starts from 42-48 days","Easy in Picking","Green fruits having 10-12 cm length","Good shelf life","Okra Hybrid with very high yield potential"],
    season:"Kharif / Rabi / Summer",
    duration:"45-48days",
    region:"All India",
    markets:"India",
    special:"Hybrid Okra",
    hybrids:[
      {name:"TMOH 333",desc:"Okra Hybrid with very high yield potential Picking starts from 45-48 days after sowing Erect with tall plant type Dark green shiny fruits having 12...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMOH-333_3D-Pouch.png"},
      {name:"TMOV 99",desc:"Okra variety with high yield potential • Tolerant to Yellow Vein Mosaic Virus (YVMV) • Picking starts from 42-48 days • Easy in Picking • Green fru...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOV-99.png"},
      {name:"TMOH 2345",desc:"• Okra Hybrid with very high yield potential • Picking starts from 45-50 days after sowing • Erect with tall plant type • Dark green shiny fruits h...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-2345.png"},
      {name:"TMOH 2322",desc:"• Okra hybrid with high yield potential • Resistant to Yellow Vein Mosaic Virus (YVMV) • Picking starts from 42-45 days • Erect with tall plant typ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-2322.png"},
      {name:"TMOH 2318",desc:"• Okra hybrid with high yield potential • Resistant to Yellow Vein Mosaic Virus (YVMV) • Picking starts from 40-45 days • Erect with tall plant typ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-2318.png"},
      {name:"TMOH 2304",desc:"• Okra hybrid with high yield potential • Early picking and picking starts from 40-42 days • Easy in Picking • Green fruits having 12-14 cm length ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-2304.png"},
      {name:"TMOV 36",desc:"• Okra variety with high yield potential • Tolerant to Yellow Vein Mosaic Virus (YVMV) • Picking starts from 42-48 days • Easy in Picking • Green f...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOV-36.png"},
      {name:"TMOH 2352",desc:"• Okra hybrid with very high yield potential • Picking starts from 42-46 days after sowing • Erect with tall plant type • Dark green shiny fruits h...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-2352.png"},
      {name:"TMOH 329",desc:"• Okra hybrid with very high yield potential • Picking starts from 45-50 days • Erect with tall plant type • Dark green shiny fruits having 12-14 c...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-329.png"},
      {name:"TMOH 314",desc:"• Okra hybrid with high yield potential • Highly tolerant to Yellow Vein Mosaic Virus (YVMV) • Picking starts from 40-44 days • Easy in Picking • G...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMOH-314.png"},
      {name:"Shivi (TMOH 307)",desc:"SHIVI (TMOH 307) • Okra hybrid with high yield potential • Early picking and picking starts from 40-42 days • Easy in Picking • Green fruits having...",img:"https://trimurti.in/wp-content/uploads/2023/10/SHIVI.png"},
      {name:"Shivi gold",desc:"SHIVI GOLD (TMOH 316) • Okra hybrid with high yield potential • Picking starts from 45-50 days • Erect with tall plant type • Dark green fruits hav...",img:"https://trimurti.in/wp-content/uploads/2023/10/shivi-gold.png"},
      {name:"Nivi (TMOH 306)",desc:"NIVI (TMOH 306) • Okra hybrid with high yield potential • Early in picking and picking starts from 40-45 days • Green fruits having length of 11-12...",img:"https://trimurti.in/wp-content/uploads/2023/10/NIVI-scaled.jpg"},
      {name:"Nivi Gold (TMOH 303)",desc:"NIVI GOLD (TMOH 303) • Okra hybrid with very high yield potential • Picking starts from 45-50 days • Erect with tall plant type • Dark green fruits...",img:"https://trimurti.in/wp-content/uploads/2023/10/Nivi-gold.png"}
    ]
  },

  // === Cucumber (4 products) ===
  {
    id:"cucumber",
    name:"Cucumber",
    category:"vegetables",
    type:"Hybrid",
    code:"TMCU",
    active:true,
    order:12,
    detailPage:false,
    description:"Cucumber hybrid for fresh market Days to first fruit picking: 45-50 days Days to first appearance of female flower after 35-40 days No. of female fruits / vine: 15-20 Fruit colour: Dark green Avera...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/TMCU-3111.png",
    features:["Cucumber hybrid for fresh market","Days to first appearance of female flower after 30-35 days","No. of female fruits / vine: 10-15","Fruit colour: Dark green","Fruit length: 18-20 cm and Fruit diameter: 4-5 cm","Fruit weight: 180-200 g"],
    duration:"45-50days",
    region:"All India",
    markets:"India",
    special:"Cucumber",
    hybrids:[
      {name:"TMCU 3111",desc:"Cucumber hybrid for fresh market Days to first fruit picking: 45-50 days Days to first appearance of female flower after 35-40 days No. of female f...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMCU-3111.png"},
      {name:"TMCU 3102",desc:"TMCU3102 • Cucumber hybrid for fresh market • Days to first appearance of female flower after 30-35 days • No. of female fruits / vine: 10-15 • Fru...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMCU-3102.png"},
      {name:"Inam (TMCU 1111)",desc:"INAM (TMCU 1111) • Cucumber hybrid for fresh market • Days to first fruit picking: 45-50 days • Days to first appearance of female flower after 32-...",img:"https://trimurti.in/wp-content/uploads/2023/10/Inam_.png"},
      {name:"Hema Plus (TMCU 1101)",desc:"HEMA+ (TMcC^Hl) • Cucumber hybrid for fresh market • Days to first appearance of male flower: 30-32 days & female flower: 32-35 days • No. of femal...",img:"https://trimurti.in/wp-content/uploads/2023/10/hemaPLUS-scaled.jpg"}
    ]
  },

  // === Bottle Gourd (4 products) ===
  {
    id:"bottle-gourd",
    name:"Bottle Gourd",
    category:"vegetables",
    type:"Hybrid",
    code:"TMBG",
    active:true,
    order:13,
    detailPage:false,
    description:"• Bottle gourd hybrid for fresh market • Medium long cylindrical fruits • Picking starts after 50-55 days of planting • Fruit length : 25 – 30 cm • Fruit weight: 0.75 – 1.0 kg • Fruits are green in...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/TMBG-3402.png",
    features:["Bottle gourd hybrid for fresh market","Medium long cylindrical fruits","Picking starts after 50-55 days of planting","Fruit length : 25 – 30 cm","Fruit weight: 0.75 – 1.0 kg","Fruits are green in colour"],
    duration:"50-55days",
    region:"All India",
    markets:"India",
    special:"Gourds",
    hybrids:[
      {name:"TMBG 3402",desc:"• Bottle gourd hybrid for fresh market • Medium long cylindrical fruits • Picking starts after 50-55 days of planting • Fruit length : 25 – 30 cm •...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMBG-3402.png"},
      {name:"Veena (TMBG 1401)",desc:"VEENA (TMBG 1401) • Bottle gourd hybrid for fresh market with high yield potential • Picking starts after 50 -55 days of planting • Long cylindrica...",img:"https://trimurti.in/wp-content/uploads/2023/10/Veena_.png"},
      {name:"Sarla (TMBG 1404)",desc:"Bulb-shaped bottle gourd hybrid for fresh market Picking starts after 55-60 days of planting Fruit weight: 1.0-1.5 kg Fruits are green in colour Mo...",img:"https://trimurti.in/wp-content/uploads/2023/10/SARLA-GOURD.png"},
      {name:"Ila 1409",desc:"ILA (TMBG 1409) • Bottle gourd hybrid for fresh market with very high yield potential • Long cylindrical fruits with very attractive green colour •...",img:"https://trimurti.in/wp-content/uploads/2023/10/Ila1409.png"}
    ]
  },

  // === Bitter Gourd (4 products) ===
  {
    id:"bitter-gourd",
    name:"Bitter Gourd",
    category:"vegetables",
    type:"Hybrid",
    code:"TMBI",
    active:true,
    order:14,
    detailPage:false,
    description:"Bitter gourd hybrid having short spindle shaped fruits Harvesting starts after 45-50 days after planting Green spiny fruits Fruit length: 5-8 cm Fruit weight: 40-50 g Good keeping and shipping qual...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/Ayesha-3D.png",
    features:["Bitter gourd hybrid having long spindle shaped fruits","Dark Green fruits are less spiny and smooth","Picking starts after 50-55 days after planting","Average fruit length is 15 – 20 cm and girth is 4-5 cm","Fruit weight: 100 – 125 g","Very good shelflife and suitable for long distance transportation"],
    duration:"45-50days",
    region:"All India",
    markets:"India",
    special:"Gourds",
    hybrids:[
      {name:"AYESHA (TMBI 1314)",desc:"Bitter gourd hybrid having short spindle shaped fruits Harvesting starts after 45-50 days after planting Green spiny fruits Fruit length: 5-8 cm Fr...",img:"https://trimurti.in/wp-content/uploads/2025/07/Ayesha-3D.png"},
      {name:"Rishta (TMBI 1304)",desc:"RISHTA (TMBI 1304) • Bitter gourd hybrid having long spindle shaped fruits • Dark Green fruits are less spiny and smooth • Picking starts after 50-...",img:"https://trimurti.in/wp-content/uploads/2023/10/trimurti-RISHTA.png"},
      {name:"Tanu (TMBI 1305)",desc:"TANU (TMBI 1305) • Bitter gourd hybrid having Short Spindle-shaped fruits. • Picking starts after 50-55 days after planting. • Green spiny fruits. ...",img:"https://trimurti.in/wp-content/uploads/2023/10/TANU.png"},
      {name:"Ista (TMBI 1301)",desc:"ISTA (TMBI1301) • Bitter gourd hybrid having long spindle shaped fruits • Picking starts after 50-55 days after planting • Green spiny fruits • Fru...",img:"https://trimurti.in/wp-content/uploads/2023/10/ISTA-NEW.png"}
    ]
  },

  // === Sponge / Ridge Gourd (3 products) ===
  {
    id:"sponge-gourd",
    name:"Sponge / Ridge Gourd",
    category:"vegetables",
    type:"Hybrid",
    code:"TMSG",
    active:true,
    order:15,
    detailPage:false,
    description:"Sponge gourd hybrid for fresh market with high yield potential Harvesting starts after 42 -46 days of planting Fruits are very attractive dark green in colour Female flower starts from 15-18th node...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/TMSG-3615-3D-POUCH.png",
    features:["Sponge gourd hybrid for fresh market with high yield potential","Picking starts after 45 -50 days of planting","Fruits are very attractive light green in colour","Female flower starts from 14-17 nodes","Female flower per vine : 15-20","Fruit weight: 150 – 160 g"],
    duration:"42-46days",
    region:"All India",
    markets:"India",
    special:"Hybrid Sponge Gourd",
    hybrids:[
      {name:"TMSG 3615",desc:"Sponge gourd hybrid for fresh market with high yield potential Harvesting starts after 42 -46 days of planting Fruits are very attractive dark gree...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMSG-3615-3D-POUCH.png"},
      {name:"Tanya (TMSG 1601)",desc:"TANYA (TMSG 1601) • Sponge gourd hybrid for fresh market with high yield potential • Picking starts after 45 -50 days of planting • Fruits are very...",img:"https://trimurti.in/wp-content/uploads/2023/10/TANYA.png"},
      {name:"Rumi (TMSG 1602)",desc:"RUMI (TMSG 1602) • Sponge gourd hybrid for fresh market with high yield potential • Picking starts after 45 -50 days of planting • Fruits are very ...",img:"https://trimurti.in/wp-content/uploads/2023/10/RUMI-3D.png"}
    ]
  },

  // === Pumpkin (3 products) ===
  {
    id:"pumpkin",
    name:"Pumpkin",
    category:"vegetables",
    type:"Hybrid",
    code:"TMPU",
    active:true,
    order:16,
    detailPage:false,
    description:"Pumpkin hybrid for fresh market Harvesting starts after 80-85 days after sowing Fruit colour is attractive mottled Fruit weight: 5-8 kg Flesh colour is yellowish orange green Good keeping and shipp...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/TMPU-1827.png",
    features:["Pumpkin hybrid with high yield and early maturity","Days to maturity: 80-90 days","Fruit shape: Flat round","Fruit weight: 2-4 kg","Fruit skin colour: Mottled green","Good keeping quality"],
    season:"Kharif / Rabi / Summer",
    duration:"80-85days",
    region:"All India",
    markets:"India",
    special:"Hybrid Pumpkin",
    hybrids:[
      {name:"TMPU 1827",desc:"Pumpkin hybrid for fresh market Harvesting starts after 80-85 days after sowing Fruit colour is attractive mottled Fruit weight: 5-8 kg Flesh colou...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMPU-1827.png"},
      {name:"Tabla (TMPU 1836)",desc:"TABLA (TMPU1836) • Pumpkin hybrid with high yield and early maturity • Days to maturity: 80-90 days • Fruit shape: Flat round • Fruit weight: 2-4 k...",img:"https://trimurti.in/wp-content/uploads/2023/10/TABLA.png"},
      {name:"Kashinath (TMPU 1818)",desc:"KASHINATH (TMPU 1818) • Pumpkin hybrid with high yield and early maturity • Days to maturity: 90-100 days • Fruit shape: Round • Fruit skin colour:...",img:"https://trimurti.in/wp-content/uploads/2023/10/KASHINATH-1.png"}
    ]
  },

  // === Cabbage (3 products) ===
  {
    id:"cabbage",
    name:"Cabbage",
    category:"vegetables",
    type:"Hybrid",
    code:"TMCH",
    active:true,
    order:17,
    detailPage:false,
    description:"Early hybrid with very high yield potential Days to maturity: 55-65 days after transplanting Head shape: Oval round shape Head is very compact Foliage & head colour is bluish green Core is very sho...",
    features:["Premium cabbage","High yield potential","Adapted to diverse conditions"],
    season:"Kharif",
    duration:"55-65days",
    region:"All India",
    markets:"India",
    special:"Hybrid Cabbage",
    hybrids:[
      {name:"TMCH 20824",desc:"Early hybrid with very high yield potential Days to maturity: 55-65 days after transplanting Head shape: Oval round shape Head is very compact Foli..."},
      {name:"REAL STAR (TMCH 20012)",desc:"Early hybrid with high yield potential Days to maturity: 55-60 days after transplanting Head shape: Oval round shape Head is very compet Foliage co...",img:"https://trimurti.in/wp-content/uploads/2025/07/Real-star-1.png"},
      {name:"POKO (TMCH 20008)",desc:"Cabbage hybrid with high yield potential Days to maturity: 65-75 days after transplanting Head Shape: Round shape Head is compact Foliage colour Bl...",img:"https://trimurti.in/wp-content/uploads/2025/07/Real-star.png"}
    ]
  },

  // === Cauliflower (2 products) ===
  {
    id:"cauliflower",
    name:"Cauliflower",
    category:"vegetables",
    type:"Hybrid",
    code:"TMCA",
    active:true,
    order:18,
    detailPage:false,
    description:"Cauliflower hybrid with very high yield potential Days to maturity: 65-75 days after transplanting Curd: Compact dome shape & Curd semi-self blanch Curd colour: White Plant habit: Semi erect Leaf c...",
    image:"https://trimurti.in/wp-content/uploads/2025/07/TMCA-21-006-CAULIFLOWER-NEW-Pouch.png",
    features:["Premium cauliflower","High yield potential","Adapted to diverse conditions"],
    duration:"65-75days",
    region:"All India",
    markets:"India",
    special:"Hybrid Cauliflower",
    hybrids:[
      {name:"TMCA 21006",desc:"Cauliflower hybrid with very high yield potential Days to maturity: 65-75 days after transplanting Curd: Compact dome shape & Curd semi-self blanch...",img:"https://trimurti.in/wp-content/uploads/2025/07/TMCA-21-006-CAULIFLOWER-NEW-Pouch.png"},
      {name:"WHITE LILY (TMCA 21009)",desc:"Cauliflower hybrid with high yield potential Days to maturity: 70-80 days after transplanting Curd: Compact dome shape & white in colour Curd semi-...",img:"https://trimurti.in/wp-content/uploads/2025/07/White-lily.png"}
    ]
  },

  // === Watermelon (10 products) ===
  {
    id:"watermelon",
    name:"Watermelon",
    category:"vegetables",
    type:"Hybrid",
    code:"TMWH",
    active:true,
    order:19,
    detailPage:false,
    description:"• Sugar baby type Watermelon hybrid • Harvesting starts after 80 – 85 days of planting • Round shaped fruits with an average weight of 7-9 kg • Dark red flesh colour and rind colour dark green • Hi...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/TMWH-2712.png",
    features:["Sugar baby type Watermelon hybrid","Harvesting starts after 80 – 85 days of planting","Round shaped fruits with an average weight of 7-9 kg","Dark red flesh colour and rind colour dark green","High BRIX and very crispy flesh","Tolerant to major pests and diseases"],
    duration:"80–85days",
    region:"All India",
    markets:"India",
    special:"Watermelon",
    hybrids:[
      {name:"TMWH 2712",desc:"• Sugar baby type Watermelon hybrid • Harvesting starts after 80 – 85 days of planting • Round shaped fruits with an average weight of 7-9 kg • Dar...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMWH-2712.png"},
      {name:"TMWH 2710",desc:"• Dragon type Watermelon hybrid • Harvesting starts after 80-85 days of planting • Oblong fruits with an average weight of 10-12 kg • Red flesh col...",img:"https://trimurti.in/wp-content/uploads/2023/10/TMWH-2710.png"},
      {name:"Balma (TMWH 2741)",desc:"BALMA(TMWH 2741) • Ice box type hybrid • Harvesting starts after 70 days after planting • Oblong shaped fruits • Average weight of 4-6 kg • Dark re...",img:"https://trimurti.in/wp-content/uploads/2023/10/BALMA.png"},
      {name:"Aasma (TMWH 2786)",desc:"AASMA (TMWH 2786) • Ice box type Watermelon hybrid • Harvesting starts after 70-75 days of planting • Oblong shaped dark green fruits with an avera...",img:"https://trimurti.in/wp-content/uploads/2023/10/Aasma_.png"},
      {name:"Vishwanath",desc:"VISHWANATH (TMRV 1610) • Mid-early maturing (Kharif: 115-120 days) Rice variety with high yield potential • Semi-erect plant habit • Number of prod...",img:"https://trimurti.in/wp-content/uploads/2023/10/Vishwanath.png"},
      {name:"Tohfa (TMWH 708)",desc:"TOHFA (TMWH 708) • Ice box type watermelon hybrid • Harvesting starts from 70-75 days after planting • Oval shaped fruits with an average weight of...",img:"https://trimurti.in/wp-content/uploads/2023/10/Tohfa_.png"},
      {name:"Kaalia gold (TMWH 704)",desc:"Ice box type watermelon hybrid with high yield potential Harvesting starts from 75-80 days after planting Oblong shaped fruits with an average weig...",img:"https://trimurti.in/wp-content/uploads/2023/10/KALIA-GOLD.png"},
      {name:"Kaabil (TMWH 711)",desc:"KAABIL(TMWH 711) • Ice box type watermelon hybrid • Harvesting starts from 75 – 80 days after planting • Oblong shaped fruits with dark green colou...",img:"https://trimurti.in/wp-content/uploads/2023/10/KAABIL.png"},
      {name:"Ishq",desc:"ISHQ (TMWH 702) • Sugar baby type hybrid with high yield potential • Harvesting starts from 75-80 days after planting • Round shaped fruits with an...",img:"https://trimurti.in/wp-content/uploads/2023/10/Ishq.png"},
      {name:"Isha (TMWH 701)",desc:"ISHA (TMWH 701) • Dragon type hybrid with more fruits per plant • Harvesting starts from 80-85 days after planting • Oblong fruits with an average ...",img:"https://trimurti.in/wp-content/uploads/2023/10/Isha.png"}
    ]
  },

  // === Sweetcorn (1 products) ===
  {
    id:"sweetcorn",
    name:"Sweetcorn",
    category:"vegetables",
    type:"Hybrid",
    code:"TMSW",
    active:true,
    order:20,
    detailPage:false,
    description:"MITHIKORN (TMMH 8712) • Sweet com hybrid for fresh market with high yield potential • Picking starts from 80 -85 days after planting • Fruit weight: 280 – 300 g • No. of rows / cob: 14-16 • No. of ...",
    image:"https://trimurti.in/wp-content/uploads/2023/10/Mithikorn.jpg",
    features:["Sweet com hybrid for fresh market with high yield potential","Picking starts from 80 -85 days after planting","Fruit weight: 280 – 300 g","No. of rows / cob: 14-16","No. of grains / row : 40-45","Good shelf-life"],
    duration:"80-85days",
    region:"All India",
    markets:"India",
    special:"Sweetcorn",
    hybrids:[
      {name:"MithiKorn",desc:"MITHIKORN (TMMH 8712) • Sweet com hybrid for fresh market with high yield potential • Picking starts from 80 -85 days after planting • Fruit weight...",img:"https://trimurti.in/wp-content/uploads/2023/10/Mithikorn.jpg"}
    ]
  },

  // === Maize & Sorghum Fodder (5 products) ===
  {
    id:"fodder",
    name:"Maize & Sorghum Fodder",
    category:"fodder",
    type:"Variety",
    code:"TMFH",
    active:true,
    order:21,
    detailPage:false,
    description:"Multi-cut SSG forage hybrid with high yield potential Good quality fodder with higher digestibility and palatability More number of thin stem tillers/plant Soft plant stem and internode Long dark g...",
    image:"https://trimurti.in/wp-content/uploads/2026/02/TMFH-1241-Compressed.webp",
    features:["Good quality fodder with higher digestibility for livestock","Multi-cut SSG hybrid with very high yield potential","Thin stem, broad and higher number of leaves / plant","Soft plant stem and internode having high digestibility and palal","Very low HCN content recorded after 40 days","Harvesting starts after 45 days from sowing"],
    region:"All India",
    markets:"India",
    special:"Fodder",
    hybrids:[
      {name:"TMFH 1241",desc:"Multi-cut SSG forage hybrid with high yield potential Good quality fodder with higher digestibility and palatability More number of thin stem tille...",img:"https://trimurti.in/wp-content/uploads/2026/02/TMFH-1241-Compressed.webp"},
      {name:"TFX 1282",desc:"Multi-cut SSG forage hybrid with high yield potential Good quality fodder with higher digestibility and palatability More number of thin stem tille...",img:"https://trimurti.in/wp-content/uploads/2023/10/TFX-PNG-.png"},
      {name:"Samata Speed (TMFH 3206)",desc:"SAMATA SPEED (TMFH 1206) • Good quality fodder with higher digestibility for livestock • Multi-cut SSG hybrid with very high yield potential • Thin...",img:"https://trimurti.in/wp-content/uploads/2023/10/SAMATA-SPEED-3D-POUCH.png"},
      {name:"Samata (TMFH 3211)",desc:"SAMATA (TMFH 3211) • Multi-cut SSG hybrid with high yield potential • Good quality fodder with higher digestibility • Thin stem and more number of ...",img:"https://trimurti.in/wp-content/uploads/2023/10/SAMATA-PNG.png"},
      {name:"Charu (TMSH 1201)",desc:"CHARU (TMSH 1201) • Multi-cut SSG hybrid with high yield potential • Good quality fodder with higher digestibility • Thin stem and more number of t...",img:"https://trimurti.in/wp-content/uploads/2023/10/Charu_3D-Pouch.png"}
    ]
  },

];

function getActiveProducts(){return PRODUCTS.filter(function(p){return p.active!==false}).sort(function(a,b){return(a.order||99)-(b.order||99)});}
function getProductsByCategory(c){return getActiveProducts().filter(function(p){return p.category===c;});}