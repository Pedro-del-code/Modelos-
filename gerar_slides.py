"""
Gerador de Slides 3D — Modelos Atômicos
Layout: Stories/Carrossel mobile-first com swipe
Three.js carregado via importmap (sem CDN externa obrigatória)
"""

import json, os

# ── Dados dos modelos ──────────────────────────────────────────────────────────

MODELOS = [
    {
        "id": "democrito",
        "nome": "Demócrito",
        "subtitulo": "O Filósofo do Átomo",
        "ano": "460–370 a.C.",
        "cor": "#00f5d4",
        "cor_rgb": "0,245,212",
        "tipo_3d": "esfera_solida",
        "descricao": "O filósofo grego Demócrito propôs que toda a matéria era composta de partículas indivisíveis chamadas <b>átomos</b> (do grego <i>atomos</i> = indivisível). Ele imaginou que entre os átomos haveria apenas o <b>vazio</b>.",
        "contexto": "Grécia Antiga, escola atomista fundada por Leucipo. Ideia puramente filosófica, sem instrumentos científicos.",
        "caracteristicas": [
            "Átomos são indivisíveis e eternos",
            "Existem diferentes formas e tamanhos de átomos",
            "Átomos se movem livremente no vazio",
            "Todas as propriedades da matéria vêm dos átomos",
        ],
        "limitacoes": "Sem base experimental. Aristóteles rejeitou a ideia, atrasando o desenvolvimento da física atômica por quase 2.000 anos.",
        "legado": "Primeiro a usar o conceito de átomo — a base de toda a química moderna.",
    },
    {
        "id": "dalton",
        "nome": "John Dalton",
        "subtitulo": "A Teoria Atômica Científica",
        "ano": "1803",
        "cor": "#f72585",
        "cor_rgb": "247,37,133",
        "tipo_3d": "esfera_dalton",
        "descricao": "Dalton retomou o átomo com base científica. Sua <b>Teoria Atômica</b> foi a primeira com suporte experimental, fundamentada nas leis de conservação da massa e das proporções definidas.",
        "contexto": "Revolução Industrial na Inglaterra. Dalton era meteorologista e chegou ao átomo estudando a composição dos gases.",
        "caracteristicas": [
            "Átomos são esferas maciças e indivisíveis",
            "Átomos do mesmo elemento são idênticos em massa",
            "Compostos formam-se pela união de átomos diferentes",
            "Reações químicas apenas reorganizam átomos",
        ],
        "limitacoes": "Não explicava eletricidade, luz emitida por gases aquecidos, nem a existência de partículas subatômicas.",
        "legado": "Fundou a química moderna como ciência quantitativa. A tabela atômica das massas vem daí.",
    },
    {
        "id": "thomson",
        "nome": "J.J. Thomson",
        "subtitulo": "Pudim de Passas",
        "ano": "1897",
        "cor": "#7209b7",
        "cor_rgb": "114,9,183",
        "tipo_3d": "pudim_passas",
        "descricao": "Com a descoberta do <b>elétron</b> em tubos de raios catódicos, Thomson provou que o átomo <b>é divisível</b>. Propôs o modelo do Pudim de Passas: carga positiva difusa com elétrons embutidos.",
        "contexto": "Era da eletricidade. Experimentos com tubos de vidro a vácuo revelaram raios catódicos — partículas de carga negativa.",
        "caracteristicas": [
            "Átomo contém elétrons de carga negativa",
            "Carga positiva distribuída uniformemente na esfera",
            "Elétrons ficam embutidos na carga positiva",
            "Átomo é eletricamente neutro no total",
        ],
        "limitacoes": "O experimento de Rutherford (1909) derrubou este modelo ao mostrar que a carga positiva é concentrada em um núcleo minúsculo.",
        "legado": "Primeira prova experimental de que o átomo tem estrutura interna. Thomson ganhou o Nobel em 1906.",
    },
    {
        "id": "rutherford",
        "nome": "Rutherford",
        "subtitulo": "Experimento da Folha de Ouro",
        "ano": "1911",
        "cor": "#f77f00",
        "cor_rgb": "247,127,0",
        "tipo_3d": "rutherford",
        "descricao": "No <b>Experimento da Folha de Ouro</b>, Rutherford bombardeou ouro com partículas alfa. A maioria atravessou, mas algumas desviaram drasticamente — provando a existência de um <b>núcleo</b> pequeno, denso e positivo.",
        "contexto": "Universidade de Manchester. Rutherford, Geiger e Marsden esperavam desvios pequenos. O resultado os surpreendeu.",
        "caracteristicas": [
            "Núcleo central pequeno, denso e positivo",
            "Núcleo concentra quase toda a massa do átomo",
            "Elétrons orbitam ao redor do núcleo",
            "O átomo é majoritariamente espaço vazio",
        ],
        "limitacoes": "Pela física clássica, elétrons em órbita irradiariam energia e colidiriam com o núcleo em apenas ~10⁻⁸ segundos.",
        "legado": "Descoberta do núcleo atômico. Base de toda a física nuclear e dos reatores atômicos.",
    },
    {
        "id": "bohr",
        "nome": "Niels Bohr",
        "subtitulo": "Órbitas Quantizadas",
        "ano": "1913",
        "cor": "#4361ee",
        "cor_rgb": "67,97,238",
        "tipo_3d": "bohr",
        "descricao": "Bohr aplicou a nascente <b>teoria quântica</b> ao modelo de Rutherford. Elétrons só podem existir em <b>órbitas fixas com energias definidas</b>. Saltos entre órbitas emitem ou absorvem luz de frequência exata.",
        "contexto": "Copenhagen, Dinamarca. Bohr trabalhou com Rutherford em Manchester e se inspirou na teoria quântica de Planck e Einstein.",
        "caracteristicas": [
            "Elétrons em órbitas circulares fixas (níveis de energia)",
            "Cada órbita tem energia quantizada e bem definida",
            "Salto para órbita menor → emissão de fóton de luz",
            "Explica com precisão o espectro de emissão do Hidrogênio",
        ],
        "limitacoes": "Falha para átomos com mais de um elétron. Não explica a forma dos orbitais nem o Princípio da Incerteza de Heisenberg.",
        "legado": "Introduziu a quantização de energia nos átomos. Bohr ganhou o Nobel em 1922 por esse modelo.",
    },
    {
        "id": "sommerfeld",
        "nome": "Sommerfeld",
        "subtitulo": "Órbitas Elípticas e Relatividade",
        "ano": "1916",
        "cor": "#e9c46a",
        "cor_rgb": "233,196,106",
        "tipo_3d": "sommerfeld",
        "descricao": "Sommerfeld aprimorou Bohr adicionando <b>órbitas elípticas</b> e efeitos relativísticos para explicar a <b>estrutura fina</b> dos espectros atômicos — pequenas divisões das linhas espectrais que Bohr não conseguia explicar.",
        "contexto": "Munique, Alemanha. A Primeira Guerra Mundial ocorria. Sommerfeld foi mentor de Heisenberg, Pauli e outros gigantes da física quântica.",
        "caracteristicas": [
            "Órbitas elípticas além das circulares de Bohr",
            "Novo número quântico azimutal (l) além do principal (n)",
            "Correções relativísticas para elétrons em alta velocidade",
            "Explica o desdobramento de linhas espectrais",
        ],
        "limitacoes": "Ainda baseado em trajetórias definidas, incompatível com o Princípio da Incerteza. Não explica o spin do elétron.",
        "legado": "Transição entre o modelo clássico e a mecânica quântica moderna. Lançou as bases dos números quânticos.",
    },
    {
        "id": "quantum",
        "nome": "Modelo Quântico",
        "subtitulo": "A Nuvem de Probabilidade",
        "ano": "1926",
        "cor": "#06d6a0",
        "cor_rgb": "6,214,160",
        "tipo_3d": "quantum",
        "descricao": "Schrödinger, Heisenberg e De Broglie desenvolveram a <b>Mecânica Quântica</b>. O elétron não tem posição ou trajetória definida — existe como uma <b>nuvem de probabilidade</b> descrita pela função de onda ψ.",
        "contexto": "Europa pós-guerra, 1925–1927. Em apenas dois anos, mentes como Einstein, Bohr, Heisenberg e Schrödinger redefiniriam a física para sempre.",
        "caracteristicas": [
            "Princípio da Incerteza: Δx·Δp ≥ ℏ/2 (posição e momento não são precisos ao mesmo tempo)",
            "Elétron tem natureza dual: onda e partícula",
            "Orbitais s, p, d, f — regiões de alta probabilidade de encontrar o elétron",
            "4 números quânticos: n (nível), l (forma), mₗ (orientação), mₛ (spin)",
        ],
        "limitacoes": "Modelo atual — extremamente preciso. Matematicamente muito complexo; para sistemas grandes usa-se aproximações.",
        "legado": "Base de toda a química moderna, eletrônica, semicondutores, lasers, ressonância magnética e tecnologia quântica.",
    },
]

# ── JavaScript 3D ──────────────────────────────────────────────────────────────

JS_3D = r"""
var _cenas = {};

function criarCena(canvasId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return null;
    var w = canvas.clientWidth || canvas.offsetWidth || 300;
    var h = canvas.clientHeight || canvas.offsetHeight || 300;
    if (w === 0 || h === 0) { w = 300; h = 260; }
    var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setSize(w, h, false);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = false;
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(52, w / h, 0.1, 1000);
    camera.position.set(0, 0, 5.5);
    scene.add(new THREE.AmbientLight(0xffffff, 0.6));
    var pl1 = new THREE.PointLight(0xffffff, 2.0, 100);
    pl1.position.set(4, 5, 5); scene.add(pl1);
    var pl2 = new THREE.PointLight(0x4488ff, 0.9, 100);
    pl2.position.set(-5, -3, -4); scene.add(pl2);
    var pl3 = new THREE.PointLight(0xff8844, 0.4, 50);
    pl3.position.set(0, -4, 3); scene.add(pl3);
    var clock = new THREE.Clock();
    return { renderer: renderer, scene: scene, camera: camera, clock: clock, w: w, h: h };
}

function mkSphere(r, c, metal, rough, emI) {
    return new THREE.Mesh(
        new THREE.SphereGeometry(r, 48, 48),
        new THREE.MeshStandardMaterial({
            color: c, metalness: metal||0, roughness: rough||0.5,
            emissive: c, emissiveIntensity: emI||0
        })
    );
}

function mkRing(innerR, outerR, cor, opac) {
    var geo = new THREE.RingGeometry(innerR, outerR, 80);
    var mat = new THREE.MeshBasicMaterial({ color: cor, side: THREE.DoubleSide, transparent: true, opacity: opac||0.25 });
    return new THREE.Mesh(geo, mat);
}

// ── Demócrito: esfera sólida + partículas flutuando ──
function criarDemocrito(cd, cor) {
    var c = new THREE.Color(cor);
    var esfera = mkSphere(1.7, c, 0.25, 0.25, 0.18);
    cd.scene.add(esfera);
    // brilho atrás
    var glow = mkSphere(1.9, c, 0, 1, 0.06);
    cd.scene.add(glow);
    // partículas ao redor
    var parts = [];
    for (var i = 0; i < 60; i++) {
        var p = new THREE.Mesh(new THREE.SphereGeometry(0.04+Math.random()*0.05, 6, 6),
            new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.4+Math.random()*0.4 }));
        var th = Math.random()*Math.PI*2, ph = Math.random()*Math.PI;
        var rv = 2.3 + Math.random()*1.2;
        p.position.set(rv*Math.sin(ph)*Math.cos(th), rv*Math.sin(ph)*Math.sin(th), rv*Math.cos(ph));
        p.userData = { th: th, ph: ph, rv: rv, spTh: (Math.random()-0.5)*0.008, spPh: (Math.random()-0.5)*0.004 };
        cd.scene.add(p); parts.push(p);
    }
    return function(t) {
        esfera.rotation.y = t*0.45;
        esfera.rotation.x = t*0.18;
        glow.rotation.y = -t*0.2;
        parts.forEach(function(p) {
            p.userData.th += p.userData.spTh;
            p.userData.ph += p.userData.spPh;
            var d = p.userData;
            p.position.set(d.rv*Math.sin(d.ph)*Math.cos(d.th), d.rv*Math.sin(d.ph)*Math.sin(d.th), d.rv*Math.cos(d.ph));
        });
    };
}

// ── Dalton: esfera maciça + wireframe + anéis de grade ──
function criarDalton(cd, cor) {
    var c = new THREE.Color(cor);
    var esfera = mkSphere(1.75, c, 0.75, 0.12, 0.18);
    cd.scene.add(esfera);
    var wire = new THREE.Mesh(new THREE.SphereGeometry(1.78, 16, 16),
        new THREE.MeshBasicMaterial({ color: 0xffffff, wireframe: true, transparent: true, opacity: 0.06 }));
    cd.scene.add(wire);
    // linhas de latitude/longitude
    [0, Math.PI/3, -Math.PI/3, Math.PI/2].forEach(function(ang) {
        var r = mkRing(1.8, 1.82, 0xffffff, 0.12);
        r.rotation.x = ang; cd.scene.add(r);
    });
    return function(t) {
        esfera.rotation.y = t*0.38;
        esfera.rotation.x = Math.sin(t*0.2)*0.15;
        wire.rotation.y = t*0.38;
        wire.rotation.x = Math.sin(t*0.2)*0.15;
    };
}

// ── Thomson: esfera translúcida + elétrons embutidos pulsando ──
function criarThomson(cd, cor) {
    var c = new THREE.Color(cor);
    var esfera = new THREE.Mesh(new THREE.SphereGeometry(1.75, 48, 48),
        new THREE.MeshStandardMaterial({
            color: c, transparent: true, opacity: 0.22,
            emissive: c, emissiveIntensity: 0.3, side: THREE.DoubleSide
        }));
    cd.scene.add(esfera);
    // camada externa fina
    var outer = new THREE.Mesh(new THREE.SphereGeometry(1.8, 32, 32),
        new THREE.MeshBasicMaterial({ color: c, wireframe: true, transparent: true, opacity: 0.08 }));
    cd.scene.add(outer);
    var eles = [];
    var auraCors = [0xffdd00, 0xffaa00, 0xfff080];
    for (var i = 0; i < 12; i++) {
        var ec = auraCors[i % auraCors.length];
        var e = mkSphere(0.14, new THREE.Color(ec), 0.2, 0.3, 0.9);
        var th = Math.random()*Math.PI*2, ph = Math.acos(2*Math.random()-1);
        var rv = Math.random()*1.45;
        e.position.set(rv*Math.sin(ph)*Math.cos(th), rv*Math.sin(ph)*Math.sin(th), rv*Math.cos(ph));
        e.userData = { th: th, ph: ph, rv: rv, sp: 0.25+Math.random()*0.45, phase: Math.random()*Math.PI*2 };
        cd.scene.add(e); eles.push(e);
    }
    return function(t) {
        esfera.rotation.y = t*0.28;
        outer.rotation.y = -t*0.15;
        eles.forEach(function(e) {
            e.userData.th += e.userData.sp*0.011;
            var d = e.userData;
            var pulse = d.rv + Math.sin(t*1.5 + d.phase)*0.08;
            e.position.set(pulse*Math.sin(d.ph)*Math.cos(d.th), pulse*Math.sin(d.ph)*Math.sin(d.th), pulse*Math.cos(d.ph));
            var sc = 1.0 + Math.sin(t*2+d.phase)*0.15;
            e.scale.setScalar(sc);
        });
    };
}

// ── Rutherford: núcleo pulsante + elétrons em órbitas elípticas 3D ──
function criarRutherford(cd, cor) {
    var c = new THREE.Color(cor);
    // núcleo composto
    var nucleo = mkSphere(0.42, c, 0.85, 0.08, 0.8);
    cd.scene.add(nucleo);
    var nucGlow = mkSphere(0.52, c, 0, 1, 0.15);
    cd.scene.add(nucGlow);
    // prótons/nêutrons no núcleo
    for (var k = 0; k < 8; k++) {
        var np = mkSphere(0.1, new THREE.Color(k%2===0 ? 0xff4444 : 0xaaaaff), 0.5, 0.3, 0.5);
        var ang = k/8 * Math.PI*2;
        np.position.set(Math.cos(ang)*0.25, Math.sin(ang)*0.25, (k%3-1)*0.1);
        cd.scene.add(np);
    }
    var orbitas = [], eles = [];
    var configs = [
        { raio: 1.2, flat: 0.52, incX: 0.0, incZ: 0.0, sp: 1.1 },
        { raio: 2.0, flat: 0.6,  incX: 1.1, incZ: 0.5, sp: 0.75 },
        { raio: 2.7, flat: 0.45, incX: -0.8,incZ: 1.0, sp: 0.5 }
    ];
    configs.forEach(function(cfg, i) {
        var pts = new THREE.EllipseCurve(0,0,cfg.raio,cfg.raio*cfg.flat,0,Math.PI*2).getPoints(100);
        var orb = new THREE.Line(
            new THREE.BufferGeometry().setFromPoints(pts.map(function(p){ return new THREE.Vector3(p.x,p.y,0); })),
            new THREE.LineBasicMaterial({ color: 0x888888, transparent: true, opacity: 0.28 })
        );
        orb.rotation.x = cfg.incX; orb.rotation.z = cfg.incZ;
        cd.scene.add(orb);
        var e = mkSphere(0.15, new THREE.Color(0x00cfff), 0.3, 0.25, 1.0);
        cd.scene.add(e);
        orbitas.push({ raio: cfg.raio, flat: cfg.flat, incX: cfg.incX, incZ: cfg.incZ, sp: cfg.sp, ang: i*2.3 });
        eles.push(e);
    });
    return function(t) {
        nucleo.rotation.y = t*1.2;
        var pulse = 1.0 + Math.sin(t*2.5)*0.06;
        nucGlow.scale.setScalar(pulse);
        orbitas.forEach(function(o, i) {
            o.ang += o.sp*0.022;
            var v = new THREE.Vector3(Math.cos(o.ang)*o.raio, Math.sin(o.ang)*o.raio*o.flat, 0);
            v.applyEuler(new THREE.Euler(o.incX, 0, o.incZ));
            eles[i].position.copy(v);
        });
    };
}

// ── Bohr: núcleo + órbitas circulares + elétrons com trail ──
function criarBohr(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.38, c, 0.85, 0.08, 0.95);
    cd.scene.add(nucleo);
    var nucGlow = mkSphere(0.48, c, 0, 1, 0.12);
    cd.scene.add(nucGlow);
    var niveis = [
        { r:1.05, n:2, inc:0, cor: new THREE.Color(0xffffff) },
        { r:1.85, n:4, inc:Math.PI/3.5, cor: new THREE.Color(0xaaddff) },
        { r:2.55, n:6, inc:Math.PI/7, cor: new THREE.Color(0x88aaff) }
    ];
    var todos = [];
    niveis.forEach(function(nv, ni) {
        // anel/disco colorido
        var ring = mkRing(nv.r-0.01, nv.r+0.01, nv.cor, 0.3);
        ring.rotation.x = nv.inc; cd.scene.add(ring);
        for (var i = 0; i < nv.n; i++) {
            var e = mkSphere(0.11, nv.cor, 0.15, 0.3, 1.0);
            e.userData = { r: nv.r, ang: (i/nv.n)*Math.PI*2, sp: 1.1-ni*0.3, inc: nv.inc };
            cd.scene.add(e); todos.push(e);
        }
    });
    return function(t) {
        nucleo.rotation.y = t*0.9;
        nucGlow.scale.setScalar(1.0 + Math.sin(t*3)*0.05);
        todos.forEach(function(e) {
            e.userData.ang += e.userData.sp * 0.027;
            var v = new THREE.Vector3(
                Math.cos(e.userData.ang)*e.userData.r,
                Math.sin(e.userData.ang)*e.userData.r, 0);
            v.applyEuler(new THREE.Euler(e.userData.inc, 0, 0));
            e.position.copy(v);
        });
    };
}

// ── Sommerfeld: órbitas elípticas multicoloridas ──
function criarSommerfeld(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.33, c, 0.85, 0.08, 0.85);
    cd.scene.add(nucleo);
    var cfgs = [
        { rx:1.1, ry:1.1, ix:0,          iy:0,          iz:0,          sp:1.4 },
        { rx:1.9, ry:0.85,ix:Math.PI/4,   iy:0,          iz:0,          sp:1.0 },
        { rx:2.3, ry:1.05,ix:Math.PI/6,   iy:Math.PI/3,  iz:0,          sp:0.72 },
        { rx:2.65,ry:0.65,ix:-Math.PI/3,  iy:Math.PI/5,  iz:Math.PI/6,  sp:0.55 },
        { rx:1.5, ry:1.3, ix:Math.PI/2,   iy:Math.PI/4,  iz:-Math.PI/5, sp:0.9 }
    ];
    var eles = [];
    cfgs.forEach(function(cfg, i) {
        var pts = new THREE.EllipseCurve(0,0,cfg.rx,cfg.ry,0,Math.PI*2).getPoints(90);
        var clr = new THREE.Color().setHSL(i/cfgs.length, 0.9, 0.62);
        var orb = new THREE.Line(
            new THREE.BufferGeometry().setFromPoints(pts.map(function(p){ return new THREE.Vector3(p.x,p.y,0); })),
            new THREE.LineBasicMaterial({ color: clr, transparent: true, opacity: 0.42 })
        );
        orb.rotation.set(cfg.ix, cfg.iy, cfg.iz); cd.scene.add(orb);
        var e = mkSphere(0.13, clr, 0.2, 0.22, 1.0);
        e.userData = { cfg: cfg, ang: i*1.3, rot: new THREE.Euler(cfg.ix, cfg.iy, cfg.iz) };
        cd.scene.add(e); eles.push(e);
    });
    return function(t) {
        nucleo.rotation.y = t*0.55;
        eles.forEach(function(e) {
            e.userData.ang += e.userData.cfg.sp * 0.022;
            var v = new THREE.Vector3(
                Math.cos(e.userData.ang)*e.userData.cfg.rx,
                Math.sin(e.userData.ang)*e.userData.cfg.ry, 0);
            v.applyEuler(e.userData.rot);
            e.position.copy(v);
        });
    };
}

// ── Quântico: nuvem de probabilidade animada ──
function criarQuantum(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.26, c, 0.6, 0.1, 1.0);
    cd.scene.add(nucleo);
    var nucGlow = mkSphere(0.38, c, 0, 1, 0.18);
    cd.scene.add(nucGlow);
    // nuvem de pontos — orbitais s, p
    var NPTS = 2200;
    var pos = new Float32Array(NPTS*3), cols = new Float32Array(NPTS*3), vels = [];
    var shells = [
        { prob: 0.3, rMin: 0.5, rMax: 1.1, hue: 0.48 },
        { prob: 0.5, rMin: 1.0, rMax: 1.9, hue: 0.52 },
        { prob: 0.2, rMin: 1.8, rMax: 2.8, hue: 0.56 }
    ];
    for (var i = 0; i < NPTS; i++) {
        var rnd = Math.random(); var shell = shells[0];
        if (rnd > 0.3 && rnd <= 0.8) shell = shells[1];
        else if (rnd > 0.8) shell = shells[2];
        var r = shell.rMin + Math.pow(Math.random(), 0.5)*(shell.rMax - shell.rMin);
        var th = Math.random()*Math.PI*2, ph = Math.acos(2*Math.random()-1);
        pos[i*3]  =r*Math.sin(ph)*Math.cos(th);
        pos[i*3+1]=r*Math.sin(ph)*Math.sin(th);
        pos[i*3+2]=r*Math.cos(ph);
        var bright = 0.3 + Math.random()*0.7;
        var clr = new THREE.Color().setHSL(shell.hue, 0.8, bright*0.6);
        cols[i*3]=clr.r; cols[i*3+1]=clr.g; cols[i*3+2]=clr.b;
        vels.push({ th: th, baseR: r, phase: Math.random()*Math.PI*2, spTh: 0.001+Math.random()*0.004 });
    }
    var geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(cols, 3));
    var cloud = new THREE.Points(geo, new THREE.PointsMaterial({
        size: 0.065, vertexColors: true, transparent: true, opacity: 0.82
    }));
    cd.scene.add(cloud);
    return function(t) {
        nucleo.rotation.y = t*1.1;
        nucGlow.scale.setScalar(1.0 + Math.sin(t*2.2)*0.07);
        var p = cloud.geometry.attributes.position.array;
        for (var i = 0; i < NPTS; i++) {
            vels[i].th += vels[i].spTh;
            var r = vels[i].baseR + Math.sin(t*0.45+vels[i].phase)*0.12;
            var ph2 = Math.acos(Math.max(-1, Math.min(1, p[i*3+1]/(r||0.001))));
            p[i*3]   = r*Math.sin(ph2)*Math.cos(vels[i].th);
            p[i*3+2] = r*Math.sin(ph2)*Math.sin(vels[i].th);
        }
        cloud.geometry.attributes.position.needsUpdate = true;
        cloud.rotation.y = t*0.035;
    };
}

var CRIADORES = {
    esfera_solida: criarDemocrito,
    esfera_dalton:  criarDalton,
    pudim_passas:   criarThomson,
    rutherford:     criarRutherford,
    bohr:           criarBohr,
    sommerfeld:     criarSommerfeld,
    quantum:        criarQuantum
};

function iniciarCena3D(id, tipo, cor) {
    var cd = criarCena('canvas-'+id);
    if (!cd) { console.warn('Canvas nao encontrado:', id); return; }
    _cenas[id] = cd;
    var animFn = CRIADORES[tipo](cd, cor);
    var running = true;
    (function loop() {
        if (!running) return;
        requestAnimationFrame(loop);
        animFn(cd.clock.getElapsedTime());
        cd.renderer.render(cd.scene, cd.camera);
    })();
}
"""

# ── HTML Template ──────────────────────────────────────────────────────────────

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:#070b12;color:#e8eaf0;font-family:'Syne',sans-serif;touch-action:pan-y}

/* Loader */
#loader{position:fixed;inset:0;background:#070b12;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:9999;transition:opacity .5s}
.ld-ring{width:52px;height:52px;border:3px solid rgba(255,255,255,.08);border-top-color:#4361ee;border-radius:50%;animation:spin .75s linear infinite}
.ld-logo{font-size:22px;font-weight:800;letter-spacing:2px;margin-bottom:28px;color:rgba(255,255,255,.85)}
.ld-logo span{color:#4361ee}
.ld-txt{margin-top:16px;font-size:10px;letter-spacing:4px;color:#4b5563;font-family:'Space Mono',monospace}
@keyframes spin{to{transform:rotate(360deg)}}

/* Barra de progresso */
#prog{position:fixed;top:0;left:0;right:0;height:3px;background:rgba(255,255,255,.05);z-index:200}
#pf{height:100%;width:0;background:#4361ee;transition:width .4s ease,background .4s ease}

/* Carrossel */
#wrap{position:fixed;inset:0;overflow:hidden}
#track{display:flex;height:100%;will-change:transform;transition:transform .42s cubic-bezier(.4,0,.2,1)}

/* Slide base */
.slide{flex:0 0 100vw;width:100vw;height:100%;display:flex;flex-direction:column;overflow:hidden}

/* Área do canvas 3D */
.canvas-area{
  flex:0 0 42%;position:relative;overflow:hidden;
  background:radial-gradient(ellipse at 50% 55%, rgba(var(--cor-rgb),.12) 0%, #070b12 70%);
}
@media(min-height:700px){.canvas-area{flex:0 0 44%}}
@media(min-height:900px){.canvas-area{flex:0 0 46%}}
/* Desktop */
@media(min-width:768px){
  .slide{flex-direction:row}
  .canvas-area{flex:0 0 48%;height:100%}
}

.canvas3d{position:absolute;inset:0;width:100%;height:100%;display:block}

.badge{
  position:absolute;top:14px;left:14px;display:flex;align-items:center;gap:8px;
  background:rgba(0,0,0,.55);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(255,255,255,.1);border-radius:99px;padding:6px 14px;
}
.bnum{font-family:'Space Mono',monospace;font-size:10px;color:#6b7280}
.bnome{font-size:12px;font-weight:700;color:var(--cor)}
.ano-tag{
  position:absolute;bottom:12px;right:14px;
  font-family:'Space Mono',monospace;font-size:10px;
  color:rgba(255,255,255,.22);letter-spacing:2px;
}

/* Linha divisória luminosa */
.divider{
  height:1px;background:linear-gradient(90deg,transparent,var(--cor),transparent);
  opacity:.3;flex-shrink:0;
}
@media(min-width:768px){
  .divider{display:none}
  .canvas-area::after{
    content:'';position:absolute;top:0;right:0;width:1px;height:100%;
    background:linear-gradient(180deg,transparent,var(--cor),transparent);
    opacity:.3;
  }
}

/* Área de informações */
.info-area{
  flex:1;overflow-y:auto;padding:20px 18px 100px;
  display:flex;flex-direction:column;gap:16px;
  scrollbar-width:none;
}
.info-area::-webkit-scrollbar{display:none}
@media(min-width:768px){.info-area{padding:28px 32px 40px}}

.subtitulo{font-size:11px;letter-spacing:3px;text-transform:uppercase;color:var(--cor);font-family:'Space Mono',monospace;margin-bottom:4px}
.titulo{font-size:26px;font-weight:800;line-height:1.1;letter-spacing:-.5px}
@media(min-width:768px){.titulo{font-size:32px}}
.desc{font-size:13.5px;line-height:1.8;color:rgba(232,234,240,.78)}

/* Contexto histórico */
.contexto-box{
  background:rgba(255,255,255,.04);border-left:2px solid var(--cor);
  border-radius:0 8px 8px 0;padding:10px 14px;
}
.contexto-box p{font-size:12.5px;color:rgba(232,234,240,.6);line-height:1.6;font-style:italic}

/* Características */
.bloco-label{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--cor);font-family:'Space Mono',monospace;margin-bottom:10px}
.chars{list-style:none;display:flex;flex-direction:column;gap:9px}
.chars li{font-size:13px;display:flex;gap:9px;line-height:1.55;align-items:flex-start}
.ck{color:var(--cor);flex-shrink:0;font-size:9px;margin-top:4px}

/* Limitações */
.lim-box{
  background:rgba(255,70,50,.06);border:1px solid rgba(255,70,50,.18);
  border-radius:10px;padding:12px 14px;display:flex;gap:10px;align-items:flex-start;
}
.lim-i{color:#ff5040;flex-shrink:0;font-size:14px;margin-top:1px}
.lim-box p{font-size:12.5px;color:rgba(232,234,240,.68);line-height:1.65}

/* Legado */
.legado-box{
  background:rgba(var(--cor-rgb),.06);border:1px solid rgba(var(--cor-rgb),.22);
  border-radius:10px;padding:12px 14px;display:flex;gap:10px;align-items:flex-start;
}
.legado-i{color:var(--cor);flex-shrink:0;font-size:14px;margin-top:1px}
.legado-box p{font-size:12.5px;color:rgba(232,234,240,.68);line-height:1.65}

/* Navegação — dots */
#nav-bar{
  position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
  display:flex;align-items:center;gap:8px;
  background:rgba(7,11,18,.85);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
  border:1px solid rgba(255,255,255,.1);
  padding:10px 20px;border-radius:99px;z-index:200;
  box-shadow:0 8px 32px rgba(0,0,0,.4);
}
.dot{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.2);cursor:pointer;transition:all .3s;flex-shrink:0}
.dot.active{background:var(--cor, #4361ee);transform:scale(1.45);box-shadow:0 0 8px var(--cor, #4361ee)}

/* Setas desktop */
.nav-arrow{
  display:none;position:fixed;top:50%;transform:translateY(-50%);
  background:rgba(7,11,18,.7);border:1px solid rgba(255,255,255,.1);
  border-radius:50%;width:44px;height:44px;font-size:20px;
  color:rgba(255,255,255,.6);cursor:pointer;
  align-items:center;justify-content:center;
  transition:all .2s;z-index:200;
}
.nav-arrow:hover{background:rgba(67,97,238,.3);color:#fff}
#arr-l{left:16px}
#arr-r{right:16px}
@media(min-width:768px){.nav-arrow{display:flex}}
"""

def gerar_html(modelos, js_3d):
    total = len(modelos)
    slides_js = json.dumps([{"id": m["id"], "tipo": m["tipo_3d"], "cor": m["cor"]} for m in modelos])

    # Slides HTML
    slides_html = ""
    for i, m in enumerate(modelos):
        chars = "".join([f'<li><span class="ck">✦</span>{c}</li>' for c in m["caracteristicas"]])
        num = str(i+1).zfill(2)
        slides_html += f"""
<div class="slide" id="slide-{m['id']}" style="--cor:{m['cor']};--cor-rgb:{m['cor_rgb']}">
  <div class="canvas-area">
    <canvas id="canvas-{m['id']}" class="canvas3d"></canvas>
    <div class="badge">
      <span class="bnum">{num}/{str(total).zfill(2)}</span>
      <span class="bnome">{m['nome']}</span>
    </div>
    <div class="ano-tag">{m['ano']}</div>
  </div>
  <div class="divider"></div>
  <div class="info-area">
    <div>
      <div class="subtitulo">{m['subtitulo']}</div>
      <h2 class="titulo">{m['nome']}</h2>
    </div>
    <p class="desc">{m['descricao']}</p>
    <div class="contexto-box"><p>📍 {m['contexto']}</p></div>
    <div class="bloco">
      <div class="bloco-label">Características</div>
      <ul class="chars">{chars}</ul>
    </div>
    <div class="lim-box">
      <span class="lim-i">⚠</span>
      <p>{m['limitacoes']}</p>
    </div>
    <div class="legado-box">
      <span class="legado-i">★</span>
      <p>{m['legado']}</p>
    </div>
  </div>
</div>"""

    # Dots HTML
    dots_html = "".join([
        f'<span class="dot {"active" if i==0 else ""}" data-idx="{i}" '
        f'style="--cor:{m["cor"]}"></span>'
        for i, m in enumerate(modelos)
    ])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta name="theme-color" content="#070b12">
<title>Modelos Atômicos 3D</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<div id="loader">
  <div class="ld-logo">ÁTOMO<span>3D</span></div>
  <div class="ld-ring"></div>
  <div class="ld-txt">CARREGANDO MODELOS…</div>
</div>

<div id="prog"><div id="pf"></div></div>

<div id="wrap">
  <div id="track">{slides_html}</div>
</div>

<div id="nav-bar">{dots_html}</div>

<button class="nav-arrow" id="arr-l" aria-label="Anterior">‹</button>
<button class="nav-arrow" id="arr-r" aria-label="Próximo">›</button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
  crossorigin="anonymous"
  onload="window._threeOk=true; appInit();"
  onerror="onThreeError()">
</script>

<script>
var MODELOS = {slides_js};
var N = MODELOS.length;
var _idx = 0;
var _iniciados = {{}};
var _track = null;

function onThreeError() {{
  document.getElementById('loader').innerHTML =
    '<p style="color:#ff5040;font-family:monospace;padding:28px;text-align:center;max-width:320px">' +
    '⚠ Não foi possível carregar o Three.js.<br><br>' +
    '<small>Verifique sua conexão com a internet e recarregue a página.</small></p>';
}}

// Timeout de segurança
setTimeout(function() {{
  if (!window._threeOk) onThreeError();
}}, 10000);

{js_3d}

// ── Navegação ──────────────────────────────────────────────────────────────
function ir(i, animado) {{
  if (i < 0 || i >= N) return;
  _idx = i;
  _track.style.transition = animado === false ? 'none' : 'transform .42s cubic-bezier(.4,0,.2,1)';
  _track.style.transform = 'translateX(' + (-_idx * 100) + 'vw)';
  document.querySelectorAll('.dot').forEach(function(d, j) {{
    d.classList.toggle('active', j === _idx);
  }});
  var pf = document.getElementById('pf');
  pf.style.width = ((_idx + 1) / N * 100) + '%';
  pf.style.background = MODELOS[_idx].cor;
  // pré-carregar vizinhos
  [_idx, _idx+1, _idx-1].forEach(carregar);
}}

function carregar(i) {{
  if (i < 0 || i >= N) return;
  var m = MODELOS[i];
  if (_iniciados[m.id]) return;
  _iniciados[m.id] = true;
  // delay para garantir que o canvas está no DOM e tem dimensões
  setTimeout(function() {{ iniciarCena3D(m.id, m.tipo, m.cor); }}, 80);
}}

// ── Touch swipe ────────────────────────────────────────────────────────────
(function() {{
  var tx0 = 0, ty0 = 0, swiping = false, baseX = 0;
  var wrap = document.getElementById('wrap');
  wrap.addEventListener('touchstart', function(e) {{
    tx0 = e.touches[0].clientX; ty0 = e.touches[0].clientY;
    swiping = true; baseX = -_idx * window.innerWidth;
  }}, {{passive: true}});
  wrap.addEventListener('touchmove', function(e) {{
    if (!swiping) return;
    var dx = e.touches[0].clientX - tx0;
    var dy = e.touches[0].clientY - ty0;
    if (Math.abs(dx) > Math.abs(dy)) {{
      e.preventDefault();
      _track.style.transition = 'none';
      _track.style.transform = 'translateX(' + (baseX + dx) + 'px)';
    }}
  }}, {{passive: false}});
  wrap.addEventListener('touchend', function(e) {{
    if (!swiping) return; swiping = false;
    var dx = e.changedTouches[0].clientX - tx0;
    ir(Math.abs(dx) > 48 ? (dx < 0 ? Math.min(_idx+1, N-1) : Math.max(_idx-1, 0)) : _idx);
  }});
}})();

// ── Teclado ────────────────────────────────────────────────────────────────
document.addEventListener('keydown', function(e) {{
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') ir(_idx+1);
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   ir(_idx-1);
}});

// ── Dots ───────────────────────────────────────────────────────────────────
document.querySelectorAll('.dot').forEach(function(d) {{
  d.addEventListener('click', function() {{ ir(+d.dataset.idx); }});
}});

// ── Setas desktop ──────────────────────────────────────────────────────────
document.getElementById('arr-l').addEventListener('click', function() {{ ir(_idx-1); }});
document.getElementById('arr-r').addEventListener('click', function() {{ ir(_idx+1); }});

// ── Resize ─────────────────────────────────────────────────────────────────
window.addEventListener('resize', function() {{
  ir(_idx, false);
  Object.keys(_cenas).forEach(function(id) {{
    var cd = _cenas[id];
    var canvas = document.getElementById('canvas-'+id);
    if (!cd || !canvas) return;
    var w = canvas.clientWidth || 300;
    var h = canvas.clientHeight || 300;
    cd.renderer.setSize(w, h, false);
    cd.camera.aspect = w / h;
    cd.camera.updateProjectionMatrix();
  }});
}});

// ── Init ───────────────────────────────────────────────────────────────────
function appInit() {{
  _track = document.getElementById('track');
  var loader = document.getElementById('loader');
  loader.style.opacity = '0';
  loader.style.pointerEvents = 'none';
  setTimeout(function() {{ loader.style.display = 'none'; }}, 500);
  ir(0, false);
}}
</script>
</body>
</html>"""

# ── Main ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "index.html")
    print("Gerando index.html…")
    html = gerar_html(MODELOS, JS_3D)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    size_kb = len(html.encode()) // 1024
    print(f"✓ Gerado: {out_path}")
    print(f"  Tamanho: {size_kb} KB")
    print(f"  Slides:  {len(MODELOS)}")
