"""
Gerador de Slides 3D - Modelos Atômicos
Layout: Stories/Carrossel mobile-first com swipe
"""

modelos = [
    {
        "id": "democrito",
        "nome": "Demócrito",
        "ano": "460–370 a.C.",
        "cor": "#00f5d4",
        "descricao": "O filósofo grego Demócrito propôs que toda matéria era composta de partículas indivisíveis chamadas <b>átomos</b> (do grego <i>atomos</i> = indivisível).",
        "caracteristicas": [
            "Átomos são indivisíveis e eternos",
            "Existem diferentes tipos de átomos",
            "Átomos se movem no vazio",
            "Modelo puramente filosófico, sem experimentos"
        ],
        "limitacoes": "Sem base experimental. Aristóteles rejeitou a ideia, atrasando o desenvolvimento por séculos.",
        "tipo_3d": "esfera_solida"
    },
    {
        "id": "dalton",
        "nome": "John Dalton",
        "ano": "1803",
        "cor": "#f72585",
        "descricao": "Dalton retomou o átomo com base científica. Sua <b>Teoria Atômica</b> foi a primeira com suporte experimental, baseada nas leis de conservação da massa.",
        "caracteristicas": [
            "Átomos são esferas maciças e indivisíveis",
            "Átomos do mesmo elemento são idênticos",
            "Compostos = união de átomos diferentes",
            "Reações químicas reorganizam átomos"
        ],
        "limitacoes": "Não explicava eletricidade, luz emitida por gases, nem partículas subatômicas.",
        "tipo_3d": "esfera_dalton"
    },
    {
        "id": "thomson",
        "nome": "J.J. Thomson",
        "ano": "1897",
        "cor": "#7209b7",
        "descricao": "Com a descoberta do <b>elétron</b> em tubos de raios catódicos, Thomson propôs o modelo do <b>Pudim de Passas</b>: esfera positiva com elétrons embutidos.",
        "caracteristicas": [
            "Átomo é divisível — contém elétrons",
            "Elétrons têm carga negativa",
            "Carga positiva distribuída uniformemente",
            "Átomo é eletricamente neutro"
        ],
        "limitacoes": "Derrubado pelo experimento de Rutherford (1909), que mostrou a carga positiva concentrada.",
        "tipo_3d": "pudim_passas"
    },
    {
        "id": "rutherford",
        "nome": "Rutherford",
        "ano": "1911",
        "cor": "#f77f00",
        "descricao": "No <b>Experimento da Folha de Ouro</b>, bombardeou ouro com partículas alfa. Algumas desviaram muito, provando existência de um <b>núcleo</b> pequeno e denso.",
        "caracteristicas": [
            "Núcleo central pequeno e denso",
            "Núcleo concentra quase toda a massa",
            "Elétrons giram ao redor do núcleo",
            "O átomo é majoritariamente vazio"
        ],
        "limitacoes": "Elétrons em órbita irradiariam energia e colidiriam com o núcleo em ~10⁻⁸ s.",
        "tipo_3d": "rutherford"
    },
    {
        "id": "bohr",
        "nome": "Niels Bohr",
        "ano": "1913",
        "cor": "#4361ee",
        "descricao": "Bohr aplicou a <b>teoria quântica</b> ao modelo de Rutherford. Elétrons só existem em <b>órbitas fixas com energias definidas</b>. Saltos entre órbitas emitem luz.",
        "caracteristicas": [
            "Elétrons em órbitas circulares fixas",
            "Cada órbita tem energia quantizada",
            "Saltos entre órbitas → emissão/absorção de luz",
            "Explica o espectro do Hidrogênio"
        ],
        "limitacoes": "Falha para átomos multieletrônicos. Não explica orbitais nem o Princípio da Incerteza.",
        "tipo_3d": "bohr"
    },
    {
        "id": "sommerfeld",
        "nome": "Sommerfeld",
        "ano": "1916",
        "cor": "#e9c46a",
        "descricao": "Sommerfeld aprimorou Bohr adicionando <b>órbitas elípticas</b> e efeitos relativísticos para explicar a estrutura fina dos espectros atômicos.",
        "caracteristicas": [
            "Órbitas elípticas além das circulares",
            "Números quânticos: n e l (azimutal)",
            "Correções relativísticas para elétrons rápidos",
            "Explica desdobramento de linhas espectrais"
        ],
        "limitacoes": "Ainda não explicava o spin do elétron nem o Princípio da Incerteza de Heisenberg.",
        "tipo_3d": "sommerfeld"
    },
    {
        "id": "quantum",
        "nome": "Modelo Quântico",
        "ano": "1926",
        "cor": "#06d6a0",
        "descricao": "Schrödinger, Heisenberg e De Broglie desenvolveram a <b>Mecânica Quântica</b>. O elétron existe como <b>nuvem de probabilidade</b> — não tem posição exata.",
        "caracteristicas": [
            "Princípio da Incerteza: Δx·Δp ≥ ℏ/2",
            "Elétron tem natureza onda-partícula",
            "Orbitais s, p, d, f — regiões de probabilidade",
            "4 números quânticos: n, l, ml, ms"
        ],
        "limitacoes": "Modelo atual. Extremamente preciso, mas matematicamente muito complexo.",
        "tipo_3d": "quantum"
    }
]

JS_3D = r"""
var cenas = {};

function criarCena(canvasId) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return null;
    var w = canvas.offsetWidth || 300;
    var h = canvas.offsetHeight || 300;
    var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setSize(w, h, false);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(55, w / h, 0.1, 1000);
    camera.position.set(0, 0, 6);
    scene.add(new THREE.AmbientLight(0xffffff, 0.5));
    var pl1 = new THREE.PointLight(0xffffff, 1.8, 100);
    pl1.position.set(5, 5, 5); scene.add(pl1);
    var pl2 = new THREE.PointLight(0x4488ff, 0.7, 100);
    pl2.position.set(-5, -3, -5); scene.add(pl2);
    var clock = new THREE.Clock();
    return { renderer: renderer, scene: scene, camera: camera, clock: clock };
}

function mkSphere(r, c, metal, rough, emI) {
    return new THREE.Mesh(
        new THREE.SphereGeometry(r, 48, 48),
        new THREE.MeshStandardMaterial({ color: c, metalness: metal||0, roughness: rough||0.5, emissive: c, emissiveIntensity: emI||0 })
    );
}

function criarDemocrito(cd, cor) {
    var c = new THREE.Color(cor);
    var esfera = mkSphere(1.8, c, 0.3, 0.2, 0.12);
    cd.scene.add(esfera);
    for (var i = 0; i < 50; i++) {
        var p = new THREE.Mesh(new THREE.SphereGeometry(0.05, 6, 6),
            new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.45 }));
        var th = Math.random()*Math.PI*2, ph = Math.random()*Math.PI, r = 2.4+Math.random();
        p.position.set(r*Math.sin(ph)*Math.cos(th), r*Math.sin(ph)*Math.sin(th), r*Math.cos(ph));
        cd.scene.add(p);
    }
    return function(t) { esfera.rotation.y = t*0.5; esfera.rotation.x = t*0.2; };
}

function criarDalton(cd, cor) {
    var c = new THREE.Color(cor);
    var esfera = mkSphere(1.8, c, 0.7, 0.1, 0.15);
    cd.scene.add(esfera);
    var wire = new THREE.Mesh(new THREE.SphereGeometry(1.83, 18, 18),
        new THREE.MeshBasicMaterial({ color: 0xffffff, wireframe: true, transparent: true, opacity: 0.07 }));
    cd.scene.add(wire);
    return function(t) { esfera.rotation.y = t*0.4; wire.rotation.y = t*0.4; };
}

function criarThomson(cd, cor) {
    var c = new THREE.Color(cor);
    var esfera = new THREE.Mesh(new THREE.SphereGeometry(1.8, 48, 48),
        new THREE.MeshStandardMaterial({ color: c, transparent: true, opacity: 0.3, emissive: c, emissiveIntensity: 0.25 }));
    cd.scene.add(esfera);
    var eles = [];
    for (var i = 0; i < 10; i++) {
        var e = mkSphere(0.16, new THREE.Color(0xffdd00), 0.3, 0.2, 0.8);
        var th = Math.random()*Math.PI*2, ph = Math.acos(2*Math.random()-1), rv = Math.random()*1.4;
        e.position.set(rv*Math.sin(ph)*Math.cos(th), rv*Math.sin(ph)*Math.sin(th), rv*Math.cos(ph));
        e.userData = { th: th, ph: ph, rv: rv, sp: 0.3+Math.random()*0.4 };
        cd.scene.add(e); eles.push(e);
    }
    return function(t) {
        esfera.rotation.y = t*0.3;
        eles.forEach(function(e) {
            e.userData.th += e.userData.sp*0.012;
            var d = e.userData;
            e.position.set(d.rv*Math.sin(d.ph)*Math.cos(d.th), d.rv*Math.sin(d.ph)*Math.sin(d.th), d.rv*Math.cos(d.ph));
        });
    };
}

function criarRutherford(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.45, c, 0.8, 0.1, 0.7);
    cd.scene.add(nucleo);
    var orbitas = [], eles = [];
    [1.2, 2.0, 2.8].forEach(function(raio, i) {
        var pts = new THREE.EllipseCurve(0,0,raio,raio*0.55,0,Math.PI*2).getPoints(80);
        var orb = new THREE.Line(
            new THREE.BufferGeometry().setFromPoints(pts.map(function(p){ return new THREE.Vector3(p.x,p.y,0); })),
            new THREE.LineBasicMaterial({ color: 0x888888, transparent: true, opacity: 0.3 })
        );
        orb.rotation.x = i*0.7 - 0.5; orb.rotation.z = i*0.4;
        cd.scene.add(orb);
        var e = mkSphere(0.16, new THREE.Color(0x00cfff), 0.3, 0.2, 0.9);
        cd.scene.add(e);
        orbitas.push({ raio: raio, incX: orb.rotation.x, incZ: orb.rotation.z, sp: 0.9-i*0.25, ang: i*2.1 });
        eles.push(e);
    });
    return function(t) {
        nucleo.rotation.y = t;
        orbitas.forEach(function(o, i) {
            o.ang += o.sp*0.022;
            var v = new THREE.Vector3(Math.cos(o.ang)*o.raio, Math.sin(o.ang)*o.raio*0.55, 0);
            v.applyEuler(new THREE.Euler(o.incX, 0, o.incZ));
            eles[i].position.copy(v);
        });
    };
}

function criarBohr(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.4, c, 0.8, 0.1, 0.9);
    cd.scene.add(nucleo);
    var niveis = [{r:1.1,n:2,inc:0},{r:1.9,n:4,inc:Math.PI/3},{r:2.6,n:4,inc:Math.PI/6}];
    var todos = [];
    niveis.forEach(function(nv, ni) {
        var pts = new THREE.EllipseCurve(0,0,nv.r,nv.r,0,Math.PI*2).getPoints(80);
        var orb = new THREE.Line(
            new THREE.BufferGeometry().setFromPoints(pts.map(function(p){ return new THREE.Vector3(p.x,p.y,0); })),
            new THREE.LineBasicMaterial({ color: c, transparent: true, opacity: 0.35 })
        );
        orb.rotation.x = nv.inc; cd.scene.add(orb);
        for (var i = 0; i < nv.n; i++) {
            var e = mkSphere(0.12, new THREE.Color(0xffffff), 0.1, 0.3, 1.0);
            e.userData = { r: nv.r, ang: (i/nv.n)*Math.PI*2, sp: 1.0-ni*0.28, inc: nv.inc };
            cd.scene.add(e); todos.push(e);
        }
    });
    return function(t) {
        nucleo.rotation.y = t;
        todos.forEach(function(e) {
            e.userData.ang += e.userData.sp*0.026;
            var v = new THREE.Vector3(Math.cos(e.userData.ang)*e.userData.r, Math.sin(e.userData.ang)*e.userData.r, 0);
            v.applyEuler(new THREE.Euler(e.userData.inc, 0, 0));
            e.position.copy(v);
        });
    };
}

function criarSommerfeld(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.35, c, 0.8, 0.1, 0.8);
    cd.scene.add(nucleo);
    var cfgs = [
        {rx:1.2,ry:1.2,ix:0,iy:0,iz:0,sp:1.3},
        {rx:1.9,ry:0.9,ix:Math.PI/4,iy:0,iz:0,sp:0.9},
        {rx:2.3,ry:1.1,ix:Math.PI/6,iy:Math.PI/3,iz:0,sp:0.65},
        {rx:2.7,ry:0.7,ix:-Math.PI/3,iy:Math.PI/5,iz:Math.PI/6,sp:0.5}
    ];
    var eles = [];
    cfgs.forEach(function(cfg, i) {
        var pts = new THREE.EllipseCurve(0,0,cfg.rx,cfg.ry,0,Math.PI*2).getPoints(80);
        var clr = new THREE.Color().setHSL(i/cfgs.length, 0.85, 0.6);
        var orb = new THREE.Line(
            new THREE.BufferGeometry().setFromPoints(pts.map(function(p){ return new THREE.Vector3(p.x,p.y,0); })),
            new THREE.LineBasicMaterial({ color: clr, transparent: true, opacity: 0.45 })
        );
        orb.rotation.set(cfg.ix, cfg.iy, cfg.iz); cd.scene.add(orb);
        var e = mkSphere(0.14, clr, 0.2, 0.2, 1.0);
        e.userData = { cfg: cfg, ang: i*1.5, rot: new THREE.Euler(cfg.ix,cfg.iy,cfg.iz) };
        cd.scene.add(e); eles.push(e);
    });
    return function(t) {
        nucleo.rotation.y = t*0.5;
        eles.forEach(function(e) {
            e.userData.ang += e.userData.cfg.sp*0.022;
            var v = new THREE.Vector3(Math.cos(e.userData.ang)*e.userData.cfg.rx, Math.sin(e.userData.ang)*e.userData.cfg.ry, 0);
            v.applyEuler(e.userData.rot);
            e.position.copy(v);
        });
    };
}

function criarQuantum(cd, cor) {
    var c = new THREE.Color(cor);
    var nucleo = mkSphere(0.28, c, 0.5, 0.1, 1.0);
    cd.scene.add(nucleo);
    var N = 1800;
    var pos = new Float32Array(N*3), cols = new Float32Array(N*3), vels = [];
    for (var i = 0; i < N; i++) {
        var r = 0.5+Math.pow(Math.random(),0.4)*2.2;
        var th = Math.random()*Math.PI*2, ph = Math.acos(2*Math.random()-1);
        pos[i*3]=r*Math.sin(ph)*Math.cos(th); pos[i*3+1]=r*Math.sin(ph)*Math.sin(th); pos[i*3+2]=r*Math.cos(ph);
        var a = 0.3+Math.random()*0.7;
        cols[i*3]=c.r*a; cols[i*3+1]=c.g*a; cols[i*3+2]=c.b*a;
        vels.push({ th: th, baseR: r, phase: Math.random()*Math.PI*2 });
    }
    var geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(cols, 3));
    var cloud = new THREE.Points(geo, new THREE.PointsMaterial({ size: 0.07, vertexColors: true, transparent: true, opacity: 0.8 }));
    cd.scene.add(cloud);
    return function(t) {
        nucleo.rotation.y = t;
        var p = cloud.geometry.attributes.position.array;
        for (var i = 0; i < N; i++) {
            vels[i].th += 0.003;
            var r = vels[i].baseR + Math.sin(t*0.5+vels[i].phase)*0.1;
            var ph2 = Math.acos(Math.max(-1, Math.min(1, p[i*3+1]/(r||0.001))));
            p[i*3]   = r*Math.sin(ph2)*Math.cos(vels[i].th);
            p[i*3+2] = r*Math.sin(ph2)*Math.sin(vels[i].th);
        }
        cloud.geometry.attributes.position.needsUpdate = true;
        cloud.rotation.y = t*0.04;
    };
}

var CRIADORES = {
    esfera_solida: criarDemocrito,
    esfera_dalton: criarDalton,
    pudim_passas: criarThomson,
    rutherford: criarRutherford,
    bohr: criarBohr,
    sommerfeld: criarSommerfeld,
    quantum: criarQuantum
};

function iniciarCena3D(id, tipo, cor) {
    var cd = criarCena('canvas-'+id);
    if (!cd) { console.warn('Canvas nao encontrado:', id); return; }
    cenas[id] = cd;
    var animFn = CRIADORES[tipo](cd, cor);
    (function loop() {
        requestAnimationFrame(loop);
        animFn(cd.clock.getElapsedTime());
        cd.renderer.render(cd.scene, cd.camera);
    })();
}
"""

def gerar_html(modelos, js_3d):
    slides_js = str([{"id": m["id"], "tipo": m["tipo_3d"], "cor": m["cor"]} for m in modelos]).replace("'", '"')

    slides_html = ""
    for i, m in enumerate(modelos):
        chars = "".join([f'<li><span class="ck">✦</span>{c}</li>' for c in m["caracteristicas"]])
        slides_html += f"""
<div class="slide" id="slide-{m['id']}" style="--cor:{m['cor']}">
  <div class="canvas-area">
    <canvas id="canvas-{m['id']}" class="canvas3d"></canvas>
    <div class="badge"><span class="bnum">0{i+1}/{len(modelos)}</span><span class="bnome">{m['nome']}</span></div>
    <div class="ano-tag">{m['ano']}</div>
  </div>
  <div class="info-area">
    <h2 class="titulo">{m['nome']}</h2>
    <p class="desc">{m['descricao']}</p>
    <div class="bloco">
      <div class="bloco-label">Características</div>
      <ul class="chars">{chars}</ul>
    </div>
    <div class="lim-box">
      <span class="lim-i">⚠</span>
      <p>{m['limitacoes']}</p>
    </div>
  </div>
</div>"""

    dots_html = "".join([
        f'<span class="dot {"active" if i==0 else ""}" data-idx="{i}" style="--cor:{m["cor"]}"></span>'
        for i, m in enumerate(modelos)
    ])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>Modelos Atômicos 3D</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;height:100%;overflow:hidden;background:#080c14;color:#e8eaf0;font-family:'Syne',sans-serif;touch-action:none}}

#loader{{position:fixed;inset:0;background:#080c14;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:9999}}
.ld-ring{{width:48px;height:48px;border:3px solid rgba(255,255,255,.1);border-top-color:#4361ee;border-radius:50%;animation:spin .8s linear infinite}}
.ld-txt{{margin-top:14px;font-size:11px;letter-spacing:3px;color:#6b7280;font-family:'Space Mono',monospace}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}

#prog{{position:fixed;top:0;left:0;right:0;height:3px;background:rgba(255,255,255,.06);z-index:200}}
#pf{{height:100%;background:#4361ee;transition:width .4s,background .4s}}

#wrap{{position:fixed;inset:0;overflow:hidden}}
#track{{display:flex;height:100%;will-change:transform}}

.slide{{flex:0 0 100vw;width:100vw;height:100%;display:flex;flex-direction:column}}

.canvas-area{{
  flex:0 0 42%;position:relative;overflow:hidden;
  background:radial-gradient(ellipse at 50% 60%, color-mix(in srgb,var(--cor) 10%,#0a0f1a),#080c14);
}}
.canvas3d{{position:absolute;inset:0;width:100%;height:100%}}
.badge{{
  position:absolute;top:12px;left:12px;display:flex;align-items:center;gap:7px;
  background:rgba(0,0,0,.5);backdrop-filter:blur(10px);
  border:1px solid rgba(255,255,255,.09);border-radius:99px;padding:5px 12px;
}}
.bnum{{font-family:'Space Mono',monospace;font-size:10px;color:#6b7280}}
.bnome{{font-size:12px;font-weight:700;color:var(--cor)}}
.ano-tag{{position:absolute;bottom:10px;right:12px;font-family:'Space Mono',monospace;font-size:10px;color:rgba(255,255,255,.25);letter-spacing:2px}}

.info-area{{flex:1;overflow-y:auto;padding:20px 18px 90px;display:flex;flex-direction:column;gap:14px;scrollbar-width:none}}
.info-area::-webkit-scrollbar{{display:none}}

.titulo{{font-size:24px;font-weight:800;line-height:1.1}}
.desc{{font-size:13.5px;line-height:1.75;color:rgba(232,234,240,.8)}}

.bloco-label{{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--cor);font-family:'Space Mono',monospace;margin-bottom:9px}}
.chars{{list-style:none;display:flex;flex-direction:column;gap:7px}}
.chars li{{font-size:13px;display:flex;gap:8px;line-height:1.5}}
.ck{{color:var(--cor);flex-shrink:0;font-size:10px;margin-top:2px}}

.lim-box{{background:rgba(255,70,50,.07);border:1px solid rgba(255,70,50,.18);border-radius:10px;padding:12px 14px;display:flex;gap:9px}}
.lim-i{{color:#ff5040;flex-shrink:0;font-size:13px}}
.lim-box p{{font-size:12.5px;color:rgba(232,234,240,.7);line-height:1.6}}

#dots{{
  position:fixed;bottom:22px;left:50%;transform:translateX(-50%);
  display:flex;align-items:center;gap:7px;
  background:rgba(8,12,20,.8);backdrop-filter:blur(16px);
  border:1px solid rgba(255,255,255,.09);
  padding:10px 18px;border-radius:99px;z-index:200;
}}
.dot{{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.2);cursor:pointer;transition:all .3s}}
.dot.active{{background:var(--cor);transform:scale(1.4)}}
</style>
</head>
<body>

<div id="loader">
  <div class="ld-ring"></div>
  <div class="ld-txt">CARREGANDO…</div>
</div>

<div id="prog"><div id="pf" style="width:{round(1/len(modelos)*100)}%"></div></div>

<div id="wrap"><div id="track">{slides_html}</div></div>

<div id="dots">{dots_html}</div>

<script>
// Inline Three.js r128 minified — carregado da CDN com fallback inline
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
  onload="window._threeOk=true;appInit()"
  onerror="document.getElementById('loader').innerHTML='<p style=color:#ff5040;font-family:monospace;padding:24px>Erro ao carregar Three.js.<br>Verifique sua conexão.</p>'">
</script>
<script>
var MODELOS = {slides_js};
var N = MODELOS.length;
var idx = 0;
var iniciados = {{}};
var cenas = {{}};

{js_3d}

var track = document.getElementById('track');

function ir(i, anim) {{
  if (i < 0 || i >= N) return;
  idx = i;
  track.style.transition = anim === false ? 'none' : 'transform .42s cubic-bezier(.4,0,.2,1)';
  track.style.transform = 'translateX(' + (-idx * 100) + 'vw)';
  document.querySelectorAll('.dot').forEach(function(d,j){{ d.classList.toggle('active', j===idx); }});
  var pf = document.getElementById('pf');
  pf.style.width = ((idx+1)/N*100) + '%';
  pf.style.background = MODELOS[idx].cor;
  carregar(idx); carregar(idx+1); carregar(idx-1);
}}

function carregar(i) {{
  if (i < 0 || i >= N) return;
  var m = MODELOS[i];
  if (iniciados[m.id]) return;
  iniciados[m.id] = true;
  // pequeno delay pra garantir que o canvas foi pintado
  setTimeout(function(){{ iniciarCena3D(m.id, m.tipo, m.cor); }}, 100);
}}

document.querySelectorAll('.dot').forEach(function(d) {{
  d.addEventListener('click', function(){{ ir(+d.dataset.idx); }});
}});

// Touch swipe
var tx0 = 0, ty0 = 0, swiping = false;
document.getElementById('wrap').addEventListener('touchstart', function(e) {{
  tx0 = e.touches[0].clientX; ty0 = e.touches[0].clientY; swiping = true;
}}, {{passive: true}});
document.getElementById('wrap').addEventListener('touchmove', function(e) {{
  if (!swiping) return;
  var dx = e.touches[0].clientX - tx0;
  var dy = e.touches[0].clientY - ty0;
  if (Math.abs(dx) > Math.abs(dy)) e.preventDefault();
  var base = -idx * window.innerWidth;
  track.style.transition = 'none';
  track.style.transform = 'translateX(' + (base + dx) + 'px)';
}}, {{passive: false}});
document.getElementById('wrap').addEventListener('touchend', function(e) {{
  if (!swiping) return; swiping = false;
  var dx = e.changedTouches[0].clientX - tx0;
  if (Math.abs(dx) > 50) ir(dx < 0 ? Math.min(idx+1, N-1) : Math.max(idx-1, 0));
  else ir(idx);
}});

document.addEventListener('keydown', function(e) {{
  if (e.key === 'ArrowRight') ir(idx+1);
  if (e.key === 'ArrowLeft') ir(idx-1);
}});

window.addEventListener('resize', function() {{
  ir(idx, false);
  Object.keys(cenas).forEach(function(id) {{
    var cd = cenas[id], c = document.getElementById('canvas-'+id);
    if (!cd || !c) return;
    cd.renderer.setSize(c.offsetWidth, c.offsetHeight, false);
    cd.camera.aspect = c.offsetWidth / c.offsetHeight;
    cd.camera.updateProjectionMatrix();
  }});
}});

function appInit() {{
  var loader = document.getElementById('loader');
  loader.style.opacity = '0';
  loader.style.transition = 'opacity .4s';
  setTimeout(function(){{ loader.style.display = 'none'; }}, 400);
  ir(0, false);
}}

// Timeout de segurança: se Three.js não carregou em 8s, mostra erro
setTimeout(function() {{
  if (!window._threeOk) {{
    document.getElementById('loader').innerHTML = '<p style="color:#ff5040;font-family:monospace;padding:24px;text-align:center">Sem conexão para carregar o Three.js.<br><br><small>Verifique sua internet e recarregue.</small></p>';
  }}
}}, 8000);
</script>
</body>
</html>"""

if __name__ == "__main__":
    print("Gerando...")
    html = gerar_html(modelos, JS_3D)
    out = "/home/claude/modelos_atomicos/index.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK: {out} ({len(html.encode())//1024} KB)")
