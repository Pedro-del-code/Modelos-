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
let cenas = {};
let animFns = {};

function criarCena(canvasId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas || canvas.clientWidth === 0) return null;
    const w = canvas.clientWidth, h = canvas.clientHeight;
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
    renderer.setSize(w, h);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(55, w / h, 0.1, 1000);
    camera.position.set(0, 0, 6);
    scene.add(new THREE.AmbientLight(0xffffff, 0.5));
    const pl1 = new THREE.PointLight(0xffffff, 1.8, 100); pl1.position.set(5, 5, 5); scene.add(pl1);
    const pl2 = new THREE.PointLight(0x4488ff, 0.7, 100); pl2.position.set(-5, -3, -5); scene.add(pl2);
    const clock = new THREE.Clock();
    return { renderer, scene, camera, clock };
}

function criarModeloDemocrito(cd, cor) {
    const c = new THREE.Color(cor);
    const esfera = new THREE.Mesh(new THREE.SphereGeometry(1.8, 64, 64),
        new THREE.MeshStandardMaterial({ color: c, metalness: 0.3, roughness: 0.2, emissive: c, emissiveIntensity: 0.12 }));
    cd.scene.add(esfera);
    for (let i = 0; i < 60; i++) {
        const p = new THREE.Mesh(new THREE.SphereGeometry(0.04, 6, 6),
            new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.5 }));
        const th = Math.random()*Math.PI*2, ph = Math.random()*Math.PI, r = 2.4+Math.random()*1.2;
        p.position.set(r*Math.sin(ph)*Math.cos(th), r*Math.sin(ph)*Math.sin(th), r*Math.cos(ph));
        cd.scene.add(p);
    }
    return t => { esfera.rotation.y = t*0.5; esfera.rotation.x = t*0.2; };
}

function criarModeloDalton(cd, cor) {
    const c = new THREE.Color(cor);
    const esfera = new THREE.Mesh(new THREE.SphereGeometry(1.8, 64, 64),
        new THREE.MeshStandardMaterial({ color: c, metalness: 0.7, roughness: 0.1, emissive: c, emissiveIntensity: 0.15 }));
    cd.scene.add(esfera);
    const wire = new THREE.Mesh(new THREE.SphereGeometry(1.82, 20, 20),
        new THREE.MeshBasicMaterial({ color: 0xffffff, wireframe: true, transparent: true, opacity: 0.07 }));
    cd.scene.add(wire);
    return t => { esfera.rotation.y = t*0.4; esfera.rotation.x = Math.sin(t*0.3)*0.2; wire.rotation.y = t*0.4; };
}

function criarModeloThomson(cd, cor) {
    const c = new THREE.Color(cor);
    const esfera = new THREE.Mesh(new THREE.SphereGeometry(1.8, 48, 48),
        new THREE.MeshStandardMaterial({ color: c, transparent: true, opacity: 0.32, emissive: c, emissiveIntensity: 0.25 }));
    cd.scene.add(esfera);
    const eletrons = [];
    for (let i = 0; i < 10; i++) {
        const e = new THREE.Mesh(new THREE.SphereGeometry(0.16, 12, 12),
            new THREE.MeshStandardMaterial({ color: 0xffff00, emissive: 0xffaa00, emissiveIntensity: 0.9 }));
        const th = Math.random()*Math.PI*2, ph = Math.acos(2*Math.random()-1), r = Math.random()*1.4;
        e.position.set(r*Math.sin(ph)*Math.cos(th), r*Math.sin(ph)*Math.sin(th), r*Math.cos(ph));
        e.userData = { th, ph, r, sp: 0.3+Math.random()*0.5 };
        cd.scene.add(e); eletrons.push(e);
    }
    return t => {
        esfera.rotation.y = t*0.3;
        eletrons.forEach(e => { e.userData.th += e.userData.sp*0.012; const {r,ph,th} = e.userData;
            e.position.set(r*Math.sin(ph)*Math.cos(th), r*Math.sin(ph)*Math.sin(th), r*Math.cos(ph)); });
    };
}

function criarModeloRutherford(cd, cor) {
    const c = new THREE.Color(cor);
    const nucleo = new THREE.Mesh(new THREE.SphereGeometry(0.45, 24, 24),
        new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.7, metalness: 0.8 }));
    cd.scene.add(nucleo);
    const orbitas = [], eletrons = [];
    [1.2, 2.0, 2.8].forEach((raio, i) => {
        const pts = new THREE.EllipseCurve(0,0,raio,raio*0.55,0,Math.PI*2).getPoints(80);
        const orb = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts.map(p=>new THREE.Vector3(p.x,p.y,0))),
            new THREE.LineBasicMaterial({ color: 0x888888, transparent: true, opacity: 0.3 }));
        orb.rotation.x = (i*0.7 - 0.5); orb.rotation.z = i*0.4;
        cd.scene.add(orb);
        const e = new THREE.Mesh(new THREE.SphereGeometry(0.16, 12, 12),
            new THREE.MeshStandardMaterial({ color: 0x00cfff, emissive: 0x0088ff, emissiveIntensity: 0.9 }));
        cd.scene.add(e);
        orbitas.push({ raio, incX: orb.rotation.x, incZ: orb.rotation.z, sp: 0.9-i*0.25, ang: i*2.1 });
        eletrons.push(e);
    });
    return t => {
        nucleo.rotation.y = t;
        orbitas.forEach((o, i) => {
            o.ang += o.sp*0.022;
            const v = new THREE.Vector3(Math.cos(o.ang)*o.raio, Math.sin(o.ang)*o.raio*0.55, 0);
            v.applyEuler(new THREE.Euler(o.incX, 0, o.incZ));
            eletrons[i].position.copy(v);
        });
    };
}

function criarModeloBohr(cd, cor) {
    const c = new THREE.Color(cor);
    const nucleo = new THREE.Mesh(new THREE.SphereGeometry(0.4, 24, 24),
        new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.9 }));
    cd.scene.add(nucleo);
    const glow = new THREE.Mesh(new THREE.SphereGeometry(0.65, 24, 24),
        new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.12 }));
    cd.scene.add(glow);
    const niveis = [{r:1.1,n:2,inc:0},{r:1.9,n:8,inc:Math.PI/3},{r:2.6,n:8,inc:Math.PI/6}];
    const todos = [];
    niveis.forEach((nv, ni) => {
        const pts = new THREE.EllipseCurve(0,0,nv.r,nv.r,0,Math.PI*2).getPoints(80);
        const orb = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts.map(p=>new THREE.Vector3(p.x,p.y,0))),
            new THREE.LineBasicMaterial({ color: c, transparent: true, opacity: 0.35 }));
        orb.rotation.x = nv.inc; cd.scene.add(orb);
        for (let i=0; i<Math.min(nv.n,4); i++) {
            const e = new THREE.Mesh(new THREE.SphereGeometry(0.12, 10, 10),
                new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: c, emissiveIntensity: 1.0 }));
            e.userData = { r: nv.r, ang: (i/Math.min(nv.n,4))*Math.PI*2, sp: 1.0-ni*0.28, inc: nv.inc };
            cd.scene.add(e); todos.push(e);
        }
    });
    return t => {
        nucleo.rotation.y = t;
        todos.forEach(e => {
            e.userData.ang += e.userData.sp*0.026;
            const v = new THREE.Vector3(Math.cos(e.userData.ang)*e.userData.r, Math.sin(e.userData.ang)*e.userData.r, 0);
            v.applyEuler(new THREE.Euler(e.userData.inc, 0, 0));
            e.position.copy(v);
        });
    };
}

function criarModeloSommerfeld(cd, cor) {
    const c = new THREE.Color(cor);
    const nucleo = new THREE.Mesh(new THREE.SphereGeometry(0.35, 24, 24),
        new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.8 }));
    cd.scene.add(nucleo);
    const cfgs = [
        {rx:1.2, ry:1.2, ix:0,    iy:0,         iz:0,         sp:1.3},
        {rx:1.9, ry:0.9, ix:Math.PI/4, iy:0,     iz:0,         sp:0.9},
        {rx:2.3, ry:1.1, ix:Math.PI/6, iy:Math.PI/3, iz:0,     sp:0.65},
        {rx:2.7, ry:0.7, ix:-Math.PI/3,iy:Math.PI/5, iz:Math.PI/6, sp:0.5},
    ];
    const eles = [];
    cfgs.forEach((cfg, i) => {
        const pts = new THREE.EllipseCurve(0,0,cfg.rx,cfg.ry,0,Math.PI*2).getPoints(80);
        const clr = new THREE.Color().setHSL(i/cfgs.length, 0.85, 0.6);
        const orb = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts.map(p=>new THREE.Vector3(p.x,p.y,0))),
            new THREE.LineBasicMaterial({ color: clr, transparent: true, opacity: 0.45 }));
        orb.rotation.set(cfg.ix, cfg.iy, cfg.iz); cd.scene.add(orb);
        const e = new THREE.Mesh(new THREE.SphereGeometry(0.14, 10, 10),
            new THREE.MeshStandardMaterial({ color: clr, emissive: clr, emissiveIntensity: 1.0 }));
        e.userData = { cfg, ang: i*1.5, rot: {x:cfg.ix, y:cfg.iy, z:cfg.iz} };
        cd.scene.add(e); eles.push(e);
    });
    return t => {
        nucleo.rotation.y = t*0.5;
        eles.forEach(e => {
            e.userData.ang += e.userData.cfg.sp*0.022;
            const {cfg, ang, rot} = e.userData;
            const v = new THREE.Vector3(Math.cos(ang)*cfg.rx, Math.sin(ang)*cfg.ry, 0);
            v.applyEuler(new THREE.Euler(rot.x, rot.y, rot.z));
            e.position.copy(v);
        });
    };
}

function criarModeloQuantum(cd, cor) {
    const c = new THREE.Color(cor);
    const nucleo = new THREE.Mesh(new THREE.SphereGeometry(0.28, 24, 24),
        new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 1.0 }));
    cd.scene.add(nucleo);
    const N = 2500;
    const pos = new Float32Array(N*3), cols = new Float32Array(N*3), vels = [];
    for (let i=0; i<N; i++) {
        const r = 0.5+Math.pow(Math.random(),0.4)*2.3;
        const th = Math.random()*Math.PI*2, ph = Math.acos(2*Math.random()-1);
        pos[i*3]=r*Math.sin(ph)*Math.cos(th); pos[i*3+1]=r*Math.sin(ph)*Math.sin(th); pos[i*3+2]=r*Math.cos(ph);
        const a = 0.3+Math.random()*0.7;
        cols[i*3]=c.r*a; cols[i*3+1]=c.g*a; cols[i*3+2]=c.b*a;
        vels.push({ th, baseR: r, phase: Math.random()*Math.PI*2 });
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos,3));
    geo.setAttribute('color', new THREE.BufferAttribute(cols,3));
    const cloud = new THREE.Points(geo, new THREE.PointsMaterial({ size:0.06, vertexColors:true, transparent:true, opacity:0.8 }));
    cd.scene.add(cloud);
    return t => {
        nucleo.rotation.y = t;
        const p = cloud.geometry.attributes.position.array;
        for (let i=0; i<N; i++) {
            vels[i].th += 0.003;
            const r = vels[i].baseR + Math.sin(t*0.5+vels[i].phase)*0.12;
            const ph2 = Math.acos(Math.max(-1,Math.min(1, p[i*3+1]/(r||0.001))));
            p[i*3]=r*Math.sin(ph2)*Math.cos(vels[i].th);
            p[i*3+2]=r*Math.sin(ph2)*Math.sin(vels[i].th);
        }
        cloud.geometry.attributes.position.needsUpdate = true;
        cloud.rotation.y = t*0.04;
    };
}

const CRIADORES = {
    esfera_solida: criarModeloDemocrito,
    esfera_dalton: criarModeloDalton,
    pudim_passas: criarModeloThomson,
    rutherford: criarModeloRutherford,
    bohr: criarModeloBohr,
    sommerfeld: criarModeloSommerfeld,
    quantum: criarModeloQuantum
};

function iniciarCena3D(id, tipo, cor) {
    const cd = criarCena('canvas-'+id);
    if (!cd) return;
    cenas[id] = cd;
    animFns[id] = CRIADORES[tipo](cd, cor);
    let mx=0, my=0;
    const canvas = document.getElementById('canvas-'+id);
    if (canvas) {
        canvas.addEventListener('mousemove', e => {
            const r = canvas.getBoundingClientRect();
            mx = ((e.clientX-r.left)/r.width - 0.5)*2;
            my = -((e.clientY-r.top)/r.height - 0.5)*2;
        });
    }
    (function loop() {
        requestAnimationFrame(loop);
        const t = cd.clock.getElapsedTime();
        cd.camera.position.x += (mx*0.4 - cd.camera.position.x)*0.05;
        cd.camera.position.y += (my*0.4 - cd.camera.position.y)*0.05;
        cd.camera.lookAt(0,0,0);
        animFns[id](t);
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
<div class="slide" id="slide-{m['id']}" data-idx="{i}" style="--cor:{m['cor']}">
  <div class="slide-canvas-area">
    <canvas id="canvas-{m['id']}" class="canvas3d"></canvas>
    <div class="slide-badge"><span class="badge-num">0{i+1}/{len(modelos)}</span> <span class="badge-nome">{m['nome']}</span></div>
    <div class="slide-ano-tag">{m['ano']}</div>
  </div>
  <div class="slide-info">
    <h2 class="info-titulo">{m['nome']}</h2>
    <p class="info-desc">{m['descricao']}</p>
    <div class="info-section">
      <div class="section-label">Características</div>
      <ul class="chars-list">{chars}</ul>
    </div>
    <div class="info-lim">
      <span class="lim-icon">⚠</span>
      <p>{m['limitacoes']}</p>
    </div>
  </div>
</div>"""

    dots_html = "".join([f'<span class="dot" data-idx="{i}" style="--cor:{m["cor"]}"></span>' for i, m in enumerate(modelos)])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Modelos Atômicos 3D</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#080c14;--surface:#0d1420;--text:#e8eaf0;--dim:#6b7280;--cor:#4361ee}}
html,body{{width:100%;height:100%;overflow:hidden;background:var(--bg);color:var(--text);font-family:'Syne',sans-serif;touch-action:pan-y}}

/* LOADER */
#loader{{position:fixed;inset:0;background:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;transition:opacity .5s}}
.ld-ring{{width:50px;height:50px;border:3px solid rgba(255,255,255,.08);border-top-color:#4361ee;border-radius:50%;animation:spin .9s linear infinite}}
.ld-txt{{margin-top:16px;font-size:11px;letter-spacing:3px;color:var(--dim);font-family:'Space Mono',monospace;text-transform:uppercase}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}

/* TRACK - carrossel horizontal */
#track-wrap{{position:fixed;inset:0;overflow:hidden}}
#track{{display:flex;width:100%;height:100%;transition:transform .45s cubic-bezier(.4,0,.2,1);will-change:transform}}

/* SLIDE */
.slide{{
  flex:0 0 100%;width:100%;height:100%;
  display:flex;flex-direction:column;
  overflow:hidden;
  position:relative;
}}

/* CANVAS AREA - top 45% */
.slide-canvas-area{{
  flex:0 0 45%;position:relative;
  background:radial-gradient(ellipse at center, color-mix(in srgb,var(--cor) 8%,#0a0f1a) 0%, var(--bg) 100%);
  border-bottom:1px solid rgba(255,255,255,.06);
}}
.canvas3d{{width:100%;height:100%;display:block}}

.slide-badge{{
  position:absolute;top:14px;left:14px;
  display:flex;align-items:center;gap:8px;
  background:rgba(0,0,0,.4);backdrop-filter:blur(8px);
  border:1px solid rgba(255,255,255,.08);
  border-radius:100px;padding:5px 12px;
}}
.badge-num{{font-family:'Space Mono',monospace;font-size:10px;color:var(--dim);letter-spacing:1px}}
.badge-nome{{font-size:12px;font-weight:700;color:var(--cor)}}

.slide-ano-tag{{
  position:absolute;bottom:14px;right:14px;
  font-family:'Space Mono',monospace;font-size:10px;
  color:rgba(255,255,255,.3);letter-spacing:2px;
}}

/* INFO AREA - bottom 55% */
.slide-info{{
  flex:1;overflow-y:auto;
  padding:22px 20px 100px;
  display:flex;flex-direction:column;gap:16px;
  scrollbar-width:none;
}}
.slide-info::-webkit-scrollbar{{display:none}}

.info-titulo{{font-size:26px;font-weight:800;line-height:1.1}}
.info-desc{{font-size:14px;line-height:1.7;color:rgba(232,234,240,.8)}}

.section-label{{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--cor);font-family:'Space Mono',monospace;margin-bottom:10px;font-weight:400}}
.chars-list{{list-style:none;display:flex;flex-direction:column;gap:7px}}
.chars-list li{{font-size:13px;display:flex;align-items:flex-start;gap:9px;line-height:1.5}}
.ck{{color:var(--cor);flex-shrink:0;margin-top:1px;font-size:10px}}

.info-lim{{
  background:rgba(255,80,60,.07);border:1px solid rgba(255,80,60,.18);
  border-radius:10px;padding:12px 14px;display:flex;gap:10px;align-items:flex-start;
}}
.lim-icon{{color:#ff5040;flex-shrink:0;font-size:14px;margin-top:1px}}
.info-lim p{{font-size:12.5px;color:rgba(232,234,240,.7);line-height:1.6}}

/* BARRA PROGRESSO */
#prog{{position:fixed;top:0;left:0;right:0;height:2px;background:rgba(255,255,255,.06);z-index:100}}
#prog-fill{{height:100%;background:var(--cor,#4361ee);transition:width .4s,background .4s}}

/* DOTS */
#dots{{
  position:fixed;bottom:28px;left:50%;transform:translateX(-50%);
  display:flex;align-items:center;gap:6px;
  background:rgba(255,255,255,.05);backdrop-filter:blur(12px);
  border:1px solid rgba(255,255,255,.08);
  padding:10px 16px;border-radius:100px;z-index:100;
}}
.dot{{
  width:7px;height:7px;border-radius:50%;
  background:rgba(255,255,255,.2);cursor:pointer;
  transition:all .3s;
}}
.dot.active{{background:var(--cor);transform:scale(1.35)}}

/* SWIPE HINT */
#hint{{
  position:fixed;bottom:72px;left:50%;transform:translateX(-50%);
  font-family:'Space Mono',monospace;font-size:10px;
  color:rgba(255,255,255,.2);letter-spacing:2px;
  animation:fadeHint 3s forwards;pointer-events:none;z-index:100;white-space:nowrap;
}}
@keyframes fadeHint{{0%{{opacity:0}}20%{{opacity:1}}80%{{opacity:1}}100%{{opacity:0}}}}
</style>
</head>
<body>

<div id="loader">
  <div class="ld-ring"></div>
  <div class="ld-txt">Carregando modelos 3D…</div>
</div>

<div id="prog"><div id="prog-fill"></div></div>

<div id="track-wrap">
  <div id="track">
    {slides_html}
  </div>
</div>

<div id="dots">{dots_html}</div>
<div id="hint">← deslize →</div>

<script>
const MODELOS = {slides_js};
const N = MODELOS.length;
let idx = 0;
let cenasOk = new Set();
let cenas = {{}};

// ===== 3D ENGINE =====
{js_3d}

// ===== NAVEGAÇÃO =====
const track = document.getElementById('track');

function irPara(i, anim=true) {{
  if (i < 0 || i >= N) return;
  idx = i;
  track.style.transition = anim ? 'transform .45s cubic-bezier(.4,0,.2,1)' : 'none';
  track.style.transform = `translateX(${{-idx*100}}%)`;

  document.querySelectorAll('.dot').forEach((d,j) => d.classList.toggle('active', j===idx));

  const fill = document.getElementById('prog-fill');
  fill.style.width = ((idx+1)/N*100)+'%';
  fill.style.background = MODELOS[idx].cor;

  preload(idx); preload(idx+1); preload(idx-1);
}}

function preload(i) {{
  if (i<0||i>=N) return;
  const m = MODELOS[i];
  if (cenasOk.has(m.id)) return;
  cenasOk.add(m.id);
  setTimeout(() => iniciarCena3D(m.id, m.tipo, m.cor), 80);
}}

document.querySelectorAll('.dot').forEach(d => {{
  d.addEventListener('click', () => irPara(+d.dataset.idx));
}});

// SWIPE / TOUCH
let tx=0, startX=0, dragging=false, moved=false;
track.addEventListener('touchstart', e => {{
  startX = e.touches[0].clientX; dragging=true; moved=false;
  track.style.transition='none';
}}, {{passive:true}});
track.addEventListener('touchmove', e => {{
  if (!dragging) return;
  const dx = e.touches[0].clientX - startX;
  if (Math.abs(dx)>5) moved=true;
  tx = -idx*window.innerWidth + dx;
  track.style.transform = `translateX(${{tx}}px)`;
}}, {{passive:true}});
track.addEventListener('touchend', e => {{
  if (!dragging) return; dragging=false;
  const dx = e.changedTouches[0].clientX - startX;
  if (moved && Math.abs(dx)>50) {{
    irPara(dx<0 ? Math.min(idx+1,N-1) : Math.max(idx-1,0));
  }} else {{
    irPara(idx);
  }}
}});

// TECLADO
document.addEventListener('keydown', e => {{
  if (e.key==='ArrowRight') irPara(idx+1);
  if (e.key==='ArrowLeft') irPara(idx-1);
}});

// RESIZE
window.addEventListener('resize', () => {{
  irPara(idx, false);
  Object.keys(cenas).forEach(id => {{
    const cd=cenas[id], c=document.getElementById('canvas-'+id);
    if(!cd||!c) return;
    cd.renderer.setSize(c.clientWidth, c.clientHeight);
    cd.camera.aspect=c.clientWidth/c.clientHeight;
    cd.camera.updateProjectionMatrix();
  }});
}});

// INIT
window.addEventListener('load', () => {{
  setTimeout(() => {{
    document.getElementById('loader').style.opacity='0';
    setTimeout(()=>document.getElementById('loader').style.display='none',500);
    irPara(0, false);
  }}, 700);
}});
</script>
</body>
</html>"""

if __name__ == "__main__":
    print("🔬 Gerando apresentação mobile 3D...")
    html = gerar_html(modelos, JS_3D)
    out = "/home/claude/modelos_atomicos/index.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Gerado: {out} ({len(html.encode())//1024} KB)")
    for m in modelos:
        print(f"   · {m['nome']} ({m['ano']})")
