// ================================================================
// TRIMURTI PRODUCT CATALOG — Edit this file to manage all products
// ================================================================
// HOW TO ADD A PRODUCT:
//   Copy a block below, paste it inside the PRODUCTS array,
//   fill in the fields, and save. The page builds itself.
//
// FIELDS:
//   id           unique slug (e.g. "maize")
//   name         product display name
//   category     "field-crops" | "vegetables" | "fodder"
//   type         "Hybrid" | "Variety"
//   code         internal product code (optional)
//   description  short description (1-2 lines)
//   features     array of key features (strings)
//   region       suitable region
//   season       suitable season
//   duration     crop duration
//   special      special traits (e.g. "Drought tolerant")
//   image        path to product image (optional)
//   pdf          path to brochure PDF (optional — place in brochures/)
//   markets      market regions (optional)
//   active       true/false — set false to hide without deleting
//   order        display order within category (lower = first)
//   detailPage   true = has own detail page at crops/{id}.html
//   hybrids      array of { name, desc }
// ================================================================

const PRODUCTS = [

  // ======================================================================
  // FIELD CROPS
  // ======================================================================
  {
    id:"maize", name:"Maize", category:"field-crops", type:"Hybrid",
    code:"TMR-MZ", active:true, order:1, detailPage:true,
    description:"High-yielding biotech and conventional maize hybrids for Kharif and Rabi seasons. Strong pest tolerance and excellent grain quality.",
    image:"images/products/maize.jpg",
    features:["Biotech & conventional options","Kharif & Rabi seasons","Excellent stay-green trait","High shelling percentage"],
    region:"Central & Southern India", season:"Kharif / Rabi", duration:"95-115 days",
    special:"Pest tolerant, drought tolerance", pdf:"brochures/maize.pdf",
    markets:"India, Nepal",
    hybrids:[
      { name:"Nagma", desc:"Biotech Hybrid — Kharif" },
      { name:"TMRH-1422", desc:"Biotech Hybrid — Rabi" },
      { name:"TMRH-871", desc:"Conventional Hybrid" }
    ]
  },
  {
    id:"rice", name:"Rice", category:"field-crops", type:"Hybrid",
    code:"TMR-RC", active:true, order:2, detailPage:true,
    description:"Premium rice hybrids across early, medium, and late duration groups. Long slender grains with excellent cooking quality.",
    features:["Long slender grains","Multiple maturity groups","High tillering","Good grain quality"],
    region:"All major rice-growing regions", season:"Kharif", duration:"100-145 days",
    special:"High yield potential", pdf:"brochures/rice.pdf",
    markets:"India, Nepal",
    hybrids:[
      { name:"TMRH-221", desc:"Early Duration (100-110 days)" },
      { name:"TMRH-335", desc:"Medium Duration (120-130 days)" },
      { name:"TMRH-448", desc:"Late Duration (140-145 days)" }
    ]
  },
  {
    id:"mustard", name:"Mustard", category:"field-crops", type:"Hybrid",
    code:"TMR-MS", active:true, order:3, detailPage:true,
    description:"High oil content mustard hybrids with excellent pod load and disease tolerance. Suitable for rainfed and irrigated conditions.",
    features:["Oil content 42-45%","Pod shattering tolerance","Good meal quality","Aphid tolerance"],
    region:"Central & Northern India", season:"Rabi", duration:"85-120 days",
    special:"High oil content", pdf:"brochures/mustard.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRH-511", desc:"Early Hybrid (100-110 days)" },
      { name:"TMRH-622", desc:"High Yield Hybrid (115-120 days)" },
      { name:"TMRH-733", desc:"Short Duration Hybrid (85-95 days)" }
    ]
  },
  {
    id:"bajra", name:"Bajra (Pearl Millet)", category:"field-crops", type:"Hybrid",
    code:"TMR-BJ", active:true, order:4, detailPage:true,
    description:"Drought-tolerant pearl millet hybrids for rainfed and dryland conditions. Excellent grain filling and dual-purpose options.",
    features:["Drought tolerance","Dual-purpose options","Good grain quality","Downy mildew tolerance"],
    region:"Arid & Semi-arid zones", season:"Kharif", duration:"75-90 days",
    special:"Drought tolerant", pdf:"brochures/bajra.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRB-101", desc:"Drought Tolerant Hybrid" },
      { name:"TMRB-202", desc:"Dual Purpose Hybrid" }
    ]
  },
  {
    id:"jowar", name:"Jowar (Sorghum)", category:"field-crops", type:"Hybrid",
    code:"TMR-JW", active:true, order:5, detailPage:true,
    description:"Grain and dual-purpose sorghum hybrids with bold, lustrous grains. Excellent threshing recovery and fodder quality.",
    features:["Bold, white grains","Dual-purpose options","Shoot fly tolerance","High biomass"],
    region:"Central & Western India", season:"Kharif / Rabi", duration:"100-115 days",
    special:"Dual purpose", pdf:"brochures/jowar.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRJ-301", desc:"Grain Hybrid (100-110 days)" },
      { name:"TMRJ-402", desc:"Dual-Purpose Hybrid (105-115 days)" }
    ]
  },
  {
    id:"sunflower", name:"Sunflower", category:"field-crops", type:"Hybrid",
    code:"TMR-SF", active:true, order:6, detailPage:true,
    description:"Oil and confectionery sunflower hybrids with excellent head size and seed filling. Suitable for Kharif and Rabi seasons.",
    features:["High oil recovery","Confectionery options","Good head size","Necrosis tolerance"],
    region:"Peninsular India", season:"Kharif / Rabi", duration:"85-100 days",
    special:"Oil & confectionery types", pdf:"brochures/sunflower.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRSF-501", desc:"Oil Hybrid (40-42% oil)" },
      { name:"TMRSF-602", desc:"Confectionery Hybrid (Striped)" }
    ]
  },
  {
    id:"cotton", name:"Cotton", category:"field-crops", type:"Hybrid",
    code:"TMR-CT", active:true, order:7, detailPage:true,
    description:"BG-II and conventional cotton hybrids with premium staple length. Effective bollworm protection and good boll retention.",
    features:["BG-II technology","Premium staple (28-32 mm)","Good boll retention","Sucking pest tolerance"],
    region:"Central & Southern India", season:"Kharif", duration:"150-170 days",
    special:"BG-II technology", pdf:"brochures/cotton.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRC-701", desc:"BG-II Hybrid (Cry1Ac+Cry2Ab)" },
      { name:"TMRC-802", desc:"Conventional Hybrid" }
    ]
  },
  {
    id:"green-gram", name:"Green Gram", category:"field-crops", type:"Variety",
    code:"TMR-GG", active:true, order:8, detailPage:true,
    description:"Early and high-yielding green gram varieties with bold, shiny grains. Synchronous maturity for cleaner harvest.",
    features:["Bold, shiny grains","Synchronous maturity","Good cooking quality","YMD tolerance"],
    region:"All India", season:"Kharif / Summer", duration:"60-70 days",
    special:"Short duration", pdf:"brochures/green-gram.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRG-901", desc:"Early Variety (60-65 days)" },
      { name:"TMRG-902", desc:"High Yield Variety (65-70 days)" }
    ]
  },
  {
    id:"black-gram", name:"Black Gram", category:"field-crops", type:"Variety",
    code:"TMR-BG", active:true, order:9, detailPage:true,
    description:"Early and high-yielding black gram varieties with bold, lustrous grains. Excellent pod filling and market-preferred quality.",
    features:["Bold, black, shiny grains","Multiple picking","Good pod filling","BLB tolerance"],
    region:"All India", season:"Kharif / Rabi", duration:"65-75 days",
    special:"Bold grain type", pdf:"brochures/black-gram.pdf",
    markets:"India",
    hybrids:[
      { name:"TMRB-951", desc:"Early Variety (65-70 days)" },
      { name:"TMRB-952", desc:"High Yield Variety (70-75 days)" }
    ]
  },

  // ======================================================================
  // VEGETABLES
  // ======================================================================
  {
    id:"tomato", name:"Tomato", category:"vegetables", type:"Hybrid",
    code:"TMR-TO", active:true, order:1,
    description:"High-yielding tomato hybrids for open-field and protected cultivation. Good fruit setting and disease tolerance.",
    features:["Open-field & protected","Good fruit setting","Disease tolerance","Market-preferred shape"],
    region:"All India", season:"Kharif / Rabi / Summer", duration:"60-75 days",
    hybrids:[
      { name:"Indeterminate", desc:"Open-field, high yield" },
      { name:"Determinate", desc:"Protected cultivation" }
    ]
  },
  {
    id:"brinjal", name:"Brinjal (Eggplant)", category:"vegetables", type:"Hybrid",
    code:"TMR-BR", active:true, order:2,
    description:"Hybrid brinjal varieties with high yield potential and excellent fruit quality. Suitable for diverse growing conditions.",
    features:["High yielding","Glossy fruits","Good shelf life","Market preferred"],
    region:"All India", season:"Kharif / Rabi", duration:"70-85 days",
    hybrids:[
      { name:"Long Purple", desc:"High-yielding, glossy" },
      { name:"Round Green", desc:"Market preferred" }
    ]
  },
  {
    id:"chilli", name:"Chilli", category:"vegetables", type:"Hybrid",
    code:"TMR-CH", active:true, order:3,
    description:"Green and red chilli hybrids with high pungency and good drying recovery. Suitable for fresh market and processing.",
    features:["High pungency","Good drying recovery","Dark green colour","High yield"],
    region:"All India", season:"Kharif / Rabi", duration:"75-90 days",
    hybrids:[
      { name:"Green Chilli", desc:"High pungency, dark green" },
      { name:"Red Chilli", desc:"Good drying recovery" }
    ]
  },
  {
    id:"okra", name:"Okra (Lady's Finger)", category:"vegetables", type:"Hybrid",
    code:"TMR-OK", active:true, order:4,
    description:"Tender, dark green okra hybrids with YVMV tolerance. Excellent field holding capacity and market preference.",
    features:["YVMV tolerant","Tender, dark green","Good field holding","High yield"],
    region:"All India", season:"Kharif / Summer", duration:"50-60 days",
    special:"YVMV tolerant",
    hybrids:[
      { name:"Early Hybrid", desc:"Tender, dark green" },
      { name:"High Yield", desc:"YVMV tolerant" }
    ]
  },
  {
    id:"bottle-gourd", name:"Bottle Gourd", category:"vegetables", type:"Hybrid",
    code:"TMR-BG", active:true, order:5,
    description:"Long and round bottle gourd hybrids with tender flesh and high yield potential.",
    features:["Tender flesh","Long & round types","High yield","Good market preference"],
    region:"All India", season:"Kharif / Summer", duration:"55-65 days",
    hybrids:[
      { name:"Long Hybrid", desc:"Tender, high yield" },
      { name:"Round Hybrid", desc:"Premium variety" }
    ]
  },
  {
    id:"ridge-gourd", name:"Ridge Gourd", category:"vegetables", type:"Hybrid",
    code:"TMR-RG", active:true, order:6,
    description:"Early and high-yielding ridge gourd hybrids with long, dark green fruits and good shelf life.",
    features:["Long, dark green fruits","Good shelf life","High yield","Early maturity"],
    region:"All India", season:"Kharif", duration:"50-60 days",
    hybrids:[
      { name:"Early Hybrid", desc:"Long, dark green" },
      { name:"High Yield", desc:"Good shelf life" }
    ]
  },
  {
    id:"cabbage", name:"Cabbage", category:"vegetables", type:"Hybrid",
    code:"TMR-CB", active:true, order:7,
    description:"Compact-headed cabbage hybrid with 60-day maturity. Good field holding and market-preferred shape.",
    features:["Compact head","60 days maturity","Good field holding","Market preferred"],
    region:"All India", season:"Rabi / Kharif", duration:"55-65 days",
    hybrids:[
      { name:"Early Hybrid", desc:"Compact head, 60 days" }
    ]
  },
  {
    id:"cauliflower", name:"Cauliflower", category:"vegetables", type:"Hybrid",
    code:"TMR-CF", active:true, order:8,
    description:"Early and late cauliflower hybrids with snow-white curds. Good curd compactness and disease tolerance.",
    features:["Snow white curds","Early & late types","Good curd compactness","Disease tolerance"],
    region:"All India", season:"Rabi / Kharif", duration:"55-75 days",
    hybrids:[
      { name:"Early Hybrid", desc:"Curd formation 55 days" },
      { name:"Late Hybrid", desc:"Snow white, 75 days" }
    ]
  },
  {
    id:"cucumber", name:"Cucumber", category:"vegetables", type:"Hybrid",
    code:"TMR-CU", active:true, order:9,
    description:"Open-field and protected cucumber hybrids with dark green fruits and high yield. Parthenocarpic options for protected cultivation.",
    features:["Open-field & protected","Parthenocarpic options","Dark green fruits","High yield"],
    region:"All India", season:"Kharif / Summer", duration:"50-60 days",
    hybrids:[
      { name:"Open-field", desc:"High yield, dark green" },
      { name:"Protected", desc:"Parthenocarpic" }
    ]
  },
  {
    id:"watermelon", name:"Watermelon", category:"vegetables", type:"Hybrid",
    code:"TMR-WM", active:true, order:10,
    description:"Red and yellow watermelon hybrids with high brix and excellent eating quality. Crimson sweet and premium types.",
    features:["Red & yellow types","High brix (12-14%)","Good shipping quality","Premium eating quality"],
    region:"All India", season:"Summer / Kharif", duration:"70-85 days",
    hybrids:[
      { name:"Red Hybrid", desc:"Crimson sweet type" },
      { name:"Yellow Hybrid", desc:"Premium, high brix" }
    ]
  },

  // ======================================================================
  // FODDER
  // ======================================================================
  {
    id:"maize-fodder", name:"Maize Fodder", category:"fodder", type:"Hybrid",
    code:"TMR-FM", active:true, order:1,
    description:"High-biomass multi-cut maize fodder hybrids for dairy and livestock. Nutritious and palatable green and dry fodder.",
    features:["Multi-cut (3-4 cuts)","High biomass","Nutritious","Palatable"],
    region:"All India", season:"Kharif / Rabi", duration:"55-65 days per cut",
    hybrids:[
      { name:"Multi-Cut Fodder", desc:"High biomass, 3-4 cuts" },
      { name:"Green Fodder", desc:"Nutritious, palatable" }
    ]
  },
  {
    id:"sorghum-fodder", name:"Sorghum Fodder", category:"fodder", type:"Variety",
    code:"TMR-FS", active:true, order:2,
    description:"Multi-cut and single-cut sorghum fodder varieties with sustained fodder supply and high dry matter content.",
    features:["Multi-cut (4-5 cuts)","High dry matter","Good regrowth","Drought tolerance"],
    region:"All India", season:"Kharif / Summer", duration:"50-60 days per cut",
    hybrids:[
      { name:"Multi-Cut Variety", desc:"Sustained supply, 4-5 cuts" },
      { name:"Single-Cut Variety", desc:"High dry matter" }
    ]
  },
  {
    id:"cowpea-fodder", name:"Cowpea Fodder", category:"fodder", type:"Variety",
    code:"TMR-FC", active:true, order:3,
    description:"Protein-rich cowpea fodder varieties for improved livestock nutrition. Dual-purpose options for fodder and green manure.",
    features:["High protein (18-20% CP)","Dual-purpose","Good biomass","Soil improvement"],
    region:"All India", season:"Kharif / Summer", duration:"45-55 days",
    hybrids:[
      { name:"Fodder Variety", desc:"Protein-rich, 18-20% CP" },
      { name:"Dual-Purpose", desc:"Fodder + green manure" }
    ]
  }
];

// Helper: get active products sorted by order
function getActiveProducts() {
  return PRODUCTS.filter(function(p) { return p.active !== false; })
    .sort(function(a, b) { return (a.order || 99) - (b.order || 99); });
}

// Helper: get products by category
function getProductsByCategory(category) {
  return getActiveProducts().filter(function(p) { return p.category === category; });
}
