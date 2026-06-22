# Quien crea y administra que en Meta (equipo de 3, modelo agencia)

> *El riesgo en Meta se propaga por vinculos, no por quien hizo clic en crear.* Repartir la creacion de activos entre tres personas no protege por si solo: lo que protege es que cada persona tenga el rol minimo necesario, acceda desde su propio dispositivo e IP con 2FA, y que las ofertas vivan aisladas. Mal hecho, tres personas co-administrando todo aumentan la superficie de vinculo en vez de bajarla.

**Equipo:** Cristobal (Cris · tech, paid media, tracking, ya administra varios Business Portfolios como agencia) · Romina (Romi · contenido, organico, estrategia, diseno) · Dalila (Dali · creativos, brand, produccion visual)
**Mercado:** USA ingles · **Nicho:** nutra/health + otros · **Modelo:** affiliate ClickBank multi-oferta (hasta 3 nichos) · **Capital:** $2-5K USD · **Prioridad #1:** anti-ban. **Fecha:** 2026-06-22

**Como leer las marcas de confianza:**
- `[FUENTE REPO]` = sale de las fuentes internas investigadas, con cita.
- `[BEST-PRACTICE Meta]` = mecanica/estandar de Meta Business 2026 verificado en fuentes oficiales o consenso de la industria, no atado a una fuente del repo.
- `[CRITERIO]` = juicio operativo de este documento donde no hay un dato exacto de fuente; se marca como tal, no se inventa.

Nota de honestidad: la nomenclatura y los nombres de permisos de abajo estan verificados contra documentacion de Meta y guias 2025-2026. Donde Meta usa internamente nombres ligeramente distintos segun la pantalla (Business Suite vs Business Settings vs API), se indica. Lo que es juicio operativo va marcado `[CRITERIO]`.

---

## 1. El principio bulletproof multi-persona

La intuicion natural es: "si Cris crea el Business Portfolio, Dali crea el pixel de cada oferta y Romi crea la pagina de Facebook, repartimos el riesgo". **Es media verdad, y la mitad falsa es peligrosa.**

**Lo que NO te protege (el mito del reparto por tipo de activo):**

- **Quien hizo clic en "crear" no es lo que Meta vincula.** Meta no banea "al que creo el pixel". Meta detecta patrones de vinculo entre cuentas y propaga restricciones por esos vinculos: mismo perfil personal administrando, mismo dispositivo/fingerprint, misma IP, misma tarjeta, mismo dominio quemado. Repartir quien crea cada activo no toca ninguna de esas senales si las tres personas siguen accediendo cruzado a todo `[FUENTE REPO, 09-errores §2.2: "una cuenta limpia puede ser flageada en horas si Facebook detecta que se accede desde el mismo fingerprint que una cuenta baneada", Multilogin]`.
- **Tres admins de todo = triple superficie de ataque.** Si Romi, Dali y Cris son admin de los mismos activos, cualquiera de los tres perfiles personales que caiga (por una cuenta personal flageada, un login raro, un dispositivo infectado) pone en riesgo todo el negocio, no solo su parte. Mas admins de todo no es mas seguro: es mas puertas de entrada al mismo cuarto `[CRITERIO]`.
- **Login cruzado anula el aislamiento.** Si Dali entra al portfolio desde el computador de Romi "un ratito para subir un creativo", acaba de unir dos fingerprints. El reparto de creacion no significo nada `[CRITERIO basado en FUENTE REPO, fingerprint]`.

**Lo que SI te protege (el modelo correcto):**

1. **Roles minimos por persona.** Nadie es admin de algo que no necesita administrar. Cris admin (porque es el operador tecnico y dueno de la raiz); Romi y Dali con acceso parcial acotado a su funcion `[BEST-PRACTICE Meta: "Only full control should be given to people who need to manage access... most team members should have partial access"]`.
2. **Cada persona desde su propio dispositivo, IP estable y 2FA.** El perfil personal de cada uno es sano, con 2FA, y siempre accede desde el mismo lugar. Nunca login cruzado `[FUENTE REPO, estructura-bulletproof §5.4 y §5.5]`.
3. **No compartir tarjeta, IP ni fingerprint entre cuentas que quieres aislar.** Es la senal #1 de propagacion de bans `[FUENTE REPO, 09-errores §2.2]`.
4. **Aislar ofertas en stacks separados** (dominio, dataset, pagina, ad account, tarjeta por oferta) y, cuando el riesgo lo amerite, en Business Portfolios separados `[FUENTE REPO, estructura-bulletproof §8]`.

> **En una linea:** el reparto de "quien crea que" es secundario. Lo que hace el negocio bulletproof es el reparto de ROLES (minimos), la higiene de ACCESO (dispositivo + IP + 2FA por persona, sin cruces) y el AISLAMIENTO por oferta. Este documento ordena las tres cosas.

---

## 2. Modelo recomendado para nuestro caso

Cris ya administra varios Business Portfolios como agencia. Eso abre dos caminos. El correcto depende de cuanto quieras mezclar el negocio affiliate con la infra de agencia de OpenClaw.

### El criterio que decide: aislamiento del riesgo nutra

El nicho nutra/health es el mas vigilado por Meta `[FUENTE REPO, 09-errores §2.4]`. Un ban agresivo puede tumbar un Business Portfolio entero. Por eso la regla madre es: **el negocio affiliate no debe colgar de la misma raiz ni del mismo portfolio que la operacion de agencia de clientes reales de OpenClaw.** Si el affiliate se quema, no puede arrastrar las cuentas de los clientes que pagan.

### Modelo recomendado (el que se monta): "portfolio affiliate dedicado, Cris owner"

```
[Perfil personal FB de Cris]   (raiz · persona real · 2FA · NO es el mismo que usa para clientes OpenClaw si se puede separar)
│
`-- [Business Portfolio AFFILIATE]   (NUEVO · dedicado · aislado de los BM de clientes de agencia)
    │   owner/admin: Cris (full control)
    │   Romi y Dali: acceso parcial, acotado a su funcion
    │
    |-- Stack Oferta 1 (dominio + dataset + pagina + ad account + tarjeta propios)
    |-- Stack Oferta 2 (idem, aislado)
    `-- Stack Oferta 3 (idem, aislado)
```

**Por que este y no otro:**

- **Owner unico = control y rendicion de cuentas claros.** Cris es el operador tecnico y trafficker; ser full control del portfolio affiliate le da manejo de billing, datasets, system users y de quien entra. `[BEST-PRACTICE Meta: full control administra settings, people, tools y assets]`
- **Aislado de la agencia.** Un Business Portfolio nuevo y dedicado al affiliate evita que un ban nutra contamine los portfolios de clientes reales. El aislamiento de cliente es regla dura de OpenClaw y aplica igual aqui `[CRITERIO + alineado a regla de aislamiento de cliente]`.
- **Romi y Dali NO entran como admin.** Entran con acceso parcial a los activos que su funcion necesita (Romi a paginas; Dali a la creacion de creativos en el ad account). Asi tres personas trabajan sin triplicar la superficie de admin `[BEST-PRACTICE Meta, partial access]`.

### Donde entra Partner Access (y donde NO ahora)

Partner Access es el mecanismo de Meta para que un Business Portfolio le de acceso a OTRO Business Portfolio a sus activos, sin que ese segundo portfolio se vuelva dueno `[BEST-PRACTICE Meta: "even if you give a partner full access, they don't own your assets; your business portfolio does"]`. Es como las agencias serias trabajan multi-cliente: cada cliente tiene su portfolio, la agencia pide partner access, y cada lado maneja a su propia gente internamente.

- **Para nuestro arranque (un equipo, un negocio, 3 personas): NO se necesita Partner Access todavia.** Romi y Dali son parte del mismo negocio, no una agencia externa. Se agregan como personas con acceso parcial dentro del portfolio affiliate. Meter Partner Access aqui agrega complejidad sin beneficio `[CRITERIO]`.
- **Partner Access SI aplica en dos escenarios futuros:**
  1. Si quieres que los activos del affiliate vivan en un portfolio y la operacion la maneje el portfolio de agencia de Cris: el portfolio affiliate (dueno) da partner access al portfolio de agencia (operador). Asi el dueno conserva la propiedad y el operador trabaja sin login compartido `[BEST-PRACTICE Meta]`.
  2. Cuando escales a 1 Business Portfolio por oferta (ver §4): cada portfolio-oferta puede dar partner access a un portfolio "central" de operacion para administrarlos todos sin volver admin personal a nadie en cada uno `[CRITERIO basado en BEST-PRACTICE Meta]`.

### Alternativa mas simple (valida si quieres minima friccion al inicio)

Un solo Business Portfolio affiliate, Cris admin, Romi y Dali con acceso parcial, y los tres stacks de oferta aislados a nivel ad account/dominio/dataset/tarjeta dentro de ese mismo portfolio. Es exactamente lo que ya define la estructura bulletproof del repo `[FUENTE REPO, estructura-bulletproof §8: "comparte la raiz (perfil + 1 BM), aisla todo lo demas por oferta"]`. Esta alternativa y el modelo recomendado son la misma cosa al arrancar; la unica diferencia es que el modelo recomendado insiste en que ese portfolio sea NUEVO y dedicado, separado de los BM de clientes de agencia.

### Alternativa que NO se recomienda

Colgar el affiliate de un Business Portfolio que ya usas para clientes de agencia. Mezcla el riesgo nutra con cuentas que pagan. Un ban puede arrastrar ambos `[CRITERIO + FUENTE REPO, propagacion de bans]`. Evitar.

---

## 3. Matriz RACI por activo de Meta

Quien CREA, quien es OWNER/ADMIN, quien tiene ACCESO y con que rol exacto de Meta, desde donde, y la regla anti-ban. Las tres personas: Cris (C), Romi (R), Dali (D).

| Activo de Meta | Quien lo CREA | Quien es OWNER / ADMIN | Quien tiene ACCESO y con que ROL exacto de Meta | Desde donde (dispositivo / IP) | Regla anti-ban |
|---|---|---|---|---|---|
| **Perfil personal de Facebook** | Cada uno el suyo (ya existen) | Cada quien es dueno del propio | Cris: raiz/admin del negocio. Romi y Dali: su perfil solo se usa para recibir acceso parcial | Cada uno SIEMPRE desde su computador + IP estable | 2FA en los 3 perfiles. Perfil sano (antiguedad, foto, actividad normal). Nunca administrar el portfolio affiliate desde un perfil/dispositivo que toco una cuenta baneada `[FUENTE REPO §5.4-5.5]` |
| **Business Portfolio (affiliate)** | Cris | Cris (rol **Full control / Admin**) | Cris: Full control. Romi y Dali NO a nivel portfolio; entran solo a nivel activo (ver abajo) | Cris, su computador + IP estable | Portfolio NUEVO, dedicado, aislado de los BM de clientes. Solo Cris full control; nadie mas admin del portfolio `[BEST-PRACTICE Meta]` |
| **Ad Account (1 por oferta)** | Cris | Cris (Admin del ad account) | Cris: rol **Admin** (en Business Settings, "Manage account" + todas las tasks). Dali: rol **Advertiser** (tasks Manage campaigns + Manage creative + View performance, SIN billing ni gestion de usuarios). Romi: opcional rol **Analyst** (solo View performance) si necesita leer resultados | Cris y Dali desde su propio equipo + IP. Romi idem si entra como Analyst | 1 tarjeta limpia por ad account. Nunca 2 nichos en el mismo ad account. Dali nunca Admin (no toca billing) `[FUENTE REPO §8 + BEST-PRACTICE Meta roles]` |
| **Dataset / Pixel + CAPI (1 por oferta)** | Cris | Cris (Admin del dataset) | Cris: control total del dataset (ver, editar eventos, conectar CAPI, generar tokens). Romi/Dali: sin acceso (no lo necesitan) | Cris, su equipo + IP | 1 dataset por oferta, eventos solo de esa oferta. Validar con compra $1 antes de gastar. El Purchase llega por CAPI/postback desde ClickBank `[FUENTE REPO §8 + funnel]` |
| **Dominio verificado (1 por oferta)** | Cris (registro y verificacion DNS) | Cris (verificado bajo el portfolio affiliate) | Cris. Romi/Dali sin rol | Cris, su equipo + IP | Verificacion por DNS bajo el portfolio. 1 dominio por oferta; un dominio quemado no arrastra a los otros `[FUENTE REPO §8]` |
| **Pagina de Facebook (1 por oferta/marca)** | Cris la crea dentro del portfolio (o Romi y Cris la reclama al portfolio) | El **portfolio affiliate** es dueno de la pagina (no la persona) | Romi: rol de Pagina con tasks de **Content** (crear/editar/publicar posts) + **Community Activity** (responder/moderar) + **Insights**, para warm-up y orgnico. Cris: Full control de la pagina (admin). Dali: sin rol o solo Content si sube creativos organicos | Romi y Cris desde su propio equipo + IP | La pagina la posee el portfolio, no el perfil de Romi. Romi calienta la pagina con engagement antes de gastar. Branding consistente con la bridge `[FUENTE REPO §4 warm-up]` |
| **Cuenta de Instagram (vinculada a la pagina)** | Cris/Romi (vincular al portfolio y a la pagina) | Portfolio affiliate | Romi: gestion de contenido IG (mismo set de tasks que pagina). Cris: admin | Romi y Cris, su equipo + IP | Vinculada al portfolio, no a un perfil personal suelto. Branding consistente `[CRITERIO]` |
| **Metodo de pago / tarjeta (1 por ad account)** | Cris (carga la tarjeta) | Cris | **Solo Cris.** Nadie mas ve ni toca billing | Cris, su equipo + IP | 1 tarjeta limpia y dedicada por ad account. NUNCA la misma tarjeta entre cuentas a aislar: Meta vincula cuentas por metodo de pago `[FUENTE REPO §8 + 09-errores]` |
| **System User (API)** | Cris (Business Settings > Users > System Users) | Cris (lo crea y administra) | System User = identidad no-humana. Rol **Admin system user** (acceso a todos los activos del portfolio) o **Employee system user** (solo activos asignados). Para affiliate: empezar con Employee, asignar solo el/los ad account que la herramienta necesita | Token corre server-to-server, no es un login humano | System User solo si conectas herramientas por API (ej. subida masiva de creativos). Token guardado en `.env`, nunca en chat/commits. Permiso minimo (Employee, no Admin, salvo necesidad real) `[FUENTE REPO §8 + BEST-PRACTICE Meta system users]` |
| **Campaign** | Cris la arma; Dali puede crear/editar bajo rol Advertiser | Cris (Admin del ad account) | Cris (Admin) y Dali (Advertiser, task Manage campaigns) pueden crear/editar campanas. Romi no | Cris y Dali, su equipo + IP | Objetivo Sales, optimizar a Purchase (no a clicks). Crear en PAUSED; nunca activar sin OK explicito `[FUENTE REPO §3 paso 12]` |
| **Ad Set** | Cris / Dali (rol Advertiser) | Cris | Cris (Admin), Dali (Advertiser) | Cris y Dali, su equipo + IP | 1 CBO broad USA aislado por oferta. Placements limpios. No matar en <24-72h `[FUENTE REPO §2 y §4]` |
| **Creativos / Ads** | **Dali los produce**; Dali los sube bajo rol Advertiser (task Manage creative); Cris valida y publica | Cris (Admin) | Dali: **Advertiser** (Manage creative + Manage campaigns + View performance). Cris: Admin. Romi: aporta angulos/copy organico pero sube via rol de Pagina, no de ad account | Dali y Cris, su equipo + IP | 3-5 ads por ad set, cada uno un angulo distinto. Disclaimer de salud en el copy de cada ad nutra. No copiar-pegar la landing/creativo del vendor `[FUENTE REPO §5.3 + §6]` |

**Nota de nomenclatura verificada:** a nivel ad account, los roles que Meta expone son **Admin**, **Advertiser** y **Analyst**, que se traducen a las tasks **Manage account** (solo Admin), **Manage campaigns**, **Manage creative** (Admin y Advertiser) y **View performance** (los tres) `[BEST-PRACTICE Meta]`. A nivel portfolio, los niveles actuales son **Full control** y **Partial access** (Meta dejo atras los nombres viejos "admin/employee" en la UI nueva de Business Suite, aunque la API y algunas pantallas de Business Settings aun muestran "admin/employee") `[BEST-PRACTICE Meta]`. A nivel Pagina, el acceso se da por tasks (Content, Community Activity, Messages, Ads, Insights) y un nivel de **Facebook access con control total** equivalente a admin de la pagina `[BEST-PRACTICE Meta]`.

---

## 4. El arbol con personas asignadas (3 ofertas)

Mismo estilo que `meta-ads-estructura-bulletproof.md`. Las marcas `[C]` Cris, `[R]` Romi, `[D]` Dali indican quien administra/opera esa rama.

```
[Perfil personal FB de Cris]   [C]  (raiz · persona real · 2FA · IP estable · el unico punto comun)
│
`-- [Business Portfolio AFFILIATE]   [C owner/full control]   (dedicado · aislado de BM de clientes)
    │      Romi [R] y Dali [D] entran como ACCESO PARCIAL a nivel activo, NO como admin del portfolio
    │
    |=== OFERTA 1 · DENTAL  (ej. ProDentim) ============================
    |   |-- Dominio ......... dailydentalfix.com        [C crea + verifica]
    |   |-- Dataset 1 + CAPI  (eventos SOLO oferta 1)    [C admin]
    |   |-- Pagina FB + IG ... "Daily Dental Fix"        [C admin de pagina · R content/warm-up/organico]
    |   |-- Tarjeta A ........ (limpia, dedicada)         [C only]
    |   `-- Ad Account 1   [C admin · D advertiser · R analyst opcional]
    |       `-- Campaign -> Ad Set -> 3-5 Ads            [C arma+publica · D crea/sube creativos]
    |
    |=== OFERTA 2 · IDIOMAS  (ej. Rocket Languages) ===================
    |   |-- Dominio ......... speakfasterguide.com        [C]
    |   |-- Dataset 2 + CAPI  (eventos SOLO oferta 2)     [C]
    |   |-- Pagina FB + IG ... "Speak Faster"             [C admin · R content/warm-up]
    |   |-- Tarjeta B ........ (limpia, dedicada)          [C only]
    |   `-- Ad Account 2   [C admin · D advertiser · R analyst opcional]
    |       `-- Campaign -> Ad Set -> 3-5 Ads             [C · D]
    |
    `=== OFERTA 3 · WEIGHT LOSS  (ej. Java Burn) ======================
        |-- Dominio ......... morningmetabolic.com        [C]
        |-- Dataset 3 + CAPI  (eventos SOLO oferta 3)     [C]
        |-- Pagina FB + IG ... "Morning Metabolic"        [C admin · R content/warm-up]
        |-- Tarjeta C ........ (limpia, dedicada)          [C only]
        `-- Ad Account 3   [C admin · D advertiser · R analyst opcional]
            `-- Campaign -> Ad Set -> 3-5 Ads             [C · D]

[System User API]   [C crea/administra]  (Employee · solo ad accounts asignados · token en .env · si hay automatizacion)
```

**Lectura del arbol:**
- **Cris [C]** es la columna vertebral: owner del portfolio, admin de cada ad account, dueno de datasets, dominios, tarjetas y system user. Es el unico que toca billing y configuracion sensible.
- **Romi [R]** opera SOLO las paginas/IG por oferta: warm-up, contenido organico, comunidad. No entra al ad account salvo como Analyst de lectura.
- **Dali [D]** opera SOLO la creacion de creativos/ads dentro de cada ad account (rol Advertiser). No toca billing, no es admin, no maneja paginas.
- El **unico punto comun** entre las tres ofertas es la raiz (perfil de Cris + el portfolio). Todo lo demas esta aislado por oferta para que un ban sea un incidente de una oferta, no el fin del negocio `[FUENTE REPO §8]`.

**Cuando partir el portfolio en 3 (aislamiento extremo):** mientras los 3 stacks viven en 1 portfolio, el aislamiento llega hasta el ad account; si cae el portfolio completo, caen los tres. Cuando una oferta gaste fuerte y perder todo el portfolio ya no sea aceptable, se separa en **1 Business Portfolio por oferta**, y se usa Partner Access para que Cris los administre todos sin volverse admin personal en cada uno `[FUENTE REPO §8 + BEST-PRACTICE Meta partner access]`.

---

## 5. Roles exactos de Meta a asignar a cada persona

Nombres reales de los permisos, por persona.

### Cris (operador tecnico, trafficker, owner)
- **Business Portfolio:** **Full control** (administra settings, people, tools y todos los activos; puede reclamar/quitar activos y dar acceso) `[BEST-PRACTICE Meta]`.
- **Cada Ad Account:** rol **Admin** (incluye la task **Manage account**: billing, usuarios, todo) `[BEST-PRACTICE Meta]`.
- **Cada Dataset/Pixel:** acceso de administracion del dataset (ver y editar eventos, conectar CAPI, generar tokens de conversiones) `[BEST-PRACTICE Meta]`.
- **Cada Pagina FB + IG:** **Facebook access con control total** (admin de la pagina) `[BEST-PRACTICE Meta]`.
- **Metodo de pago:** unico autorizado a ver/editar billing `[FUENTE REPO §8]`.
- **System User:** lo crea y administra; genera tokens; asigna activos `[BEST-PRACTICE Meta]`.

### Romi (contenido, organico, warm-up, estrategia)
- **A nivel portfolio:** **Partial access** (no full control, no puede agregar admins) `[BEST-PRACTICE Meta]`.
- **Cada Pagina FB + IG:** acceso por tasks: **Content** (crear, editar, publicar posts y stories), **Community Activity** (responder comentarios, moderar), **Insights** (ver performance). Esto le permite el warm-up y la operacion organica sin ser admin de la pagina `[BEST-PRACTICE Meta]`.
- **Ad Account (opcional):** rol **Analyst** (solo **View performance**) si necesita leer resultados de campana. Nunca Advertiser ni Admin `[BEST-PRACTICE Meta]`.
- **Lo que NO tiene:** billing, gestion de usuarios, edicion de datasets, creacion de campanas.

### Dali (creativos, brand, produccion visual)
- **A nivel portfolio:** **Partial access** `[BEST-PRACTICE Meta]`.
- **Cada Ad Account:** rol **Advertiser** = tasks **Manage campaigns** + **Manage creative** + **View performance**. Puede crear/editar campanas, ad sets y subir creativos a la biblioteca, ver resultados. NO puede tocar billing ni usuarios (eso es task **Manage account**, solo Admin) `[BEST-PRACTICE Meta]`.
- **Biblioteca de creativos:** cubierta por **Manage creative** dentro del rol Advertiser `[BEST-PRACTICE Meta]`.
- **Lo que NO tiene:** billing, gestion de usuarios, full control del portfolio, admin de paginas.

### System User (no es persona; lo administra Cris)
- **Tipo:** **Employee system user** (acceso solo a los activos que se le asignen), no Admin system user, salvo que una herramienta requiera acceso a todo el portfolio `[BEST-PRACTICE Meta: "employee system users must be granted access to individual assets"]`.
- **Asignacion:** solo el/los ad account que la automatizacion necesita, con las tasks minimas.
- **Token:** se genera una vez, se guarda en `.env` local, nunca en chat ni commits. Los tokens de system user no expiran como los humanos (1-2h cortos / 60d largos), por eso sirven para server-to-server `[BEST-PRACTICE Meta]`.

---

## 6. Reglas anti-ban multi-persona (criticas)

1. **Cada persona, su propio dispositivo + IP estable + 2FA. Sin excepciones.** Cris desde el equipo de Cris, Romi desde el de Romi, Dali desde el de Dali, cada uno con su IP habitual. 2FA en los tres perfiles personales. Es la base de toda la higiene `[FUENTE REPO §5.4-5.5]`.

2. **NUNCA login cruzado.** Dali no entra "un ratito" desde el computador de Romi. Cris no administra desde un equipo prestado. Cada login cruzado une dos fingerprints y anula el aislamiento `[FUENTE REPO, fingerprint Multilogin]`.

3. **NUNCA compartir tarjeta.** 1 tarjeta limpia y dedicada por ad account, todas a nombre/control de Cris pero distintas entre si. Compartir tarjeta entre cuentas es una de las senales con que Meta las vincula y propaga bans `[FUENTE REPO §8 + 09-errores §2.2]`.

4. **Acceso por activo, nunca compartir contrasenas.** Romi y Dali entran con SU cuenta y su rol parcial. Nunca se pasa el usuario/clave de Cris. Compartir login es exactamente lo que Meta penaliza y lo que Partner Access/roles existen para evitar `[BEST-PRACTICE Meta]`.

5. **El perfil de Cris es el punto critico, trataselo como tal.** Al ser owner del portfolio y admin de todo, si el perfil personal de Cris cae, cae el negocio entero. Por eso: 2FA fuerte, dispositivo limpio, IP estable, cero actividad de riesgo en ese perfil, y NO usarlo para experimentos o cuentas descartables. La concentracion de poder en Cris es buena para el control pero peligrosa para la resiliencia: es el single point of failure `[CRITERIO + FUENTE REPO §1 raiz]`.

6. **Roles minimos = menos puertas.** Romi sin acceso al ad account (salvo Analyst). Dali sin billing ni admin. Nadie admin de algo que no opera. Cada permiso de mas es una superficie de mas `[BEST-PRACTICE Meta]`.

7. **Plan de contingencia si cae el perfil de UNA persona:**
   - **Si cae Dali o Romi (acceso parcial):** el dano es acotado. Cris (full control) revoca el acceso del perfil caido en Business Settings > People, y reasigna las tasks a un perfil limpio de esa persona (o asume Cris temporalmente). El negocio sigue. Por eso importa que NO sean admin: su caida no tumba el portfolio `[CRITERIO + BEST-PRACTICE Meta]`.
   - **Si cae el perfil de Cris (full control):** es el escenario grave. Mitigacion: tener un **segundo perfil de confianza con full control del portfolio** como respaldo (un perfil sano, real, de Romi o de un socio, con 2FA, que NO se use para operar dia a dia, solo como llave de recuperacion). Asi, si el perfil principal de Cris cae, ese segundo full control puede recuperar el portfolio y reasignar. Sin un segundo admin, perder el perfil de Cris = perder el portfolio `[CRITERIO]`. (Matiz: agregar un segundo full control sube levemente la superficie; el trade-off vale la pena solo si ese perfil esta impecable y casi no se loguea.)
   - **Si cae un ad account (no el perfil):** los otros stacks siguen porque estan aislados. Se documenta, se pausa, y se evalua apelacion. No se accede al resto desde el mismo contexto del que cayo `[FUENTE REPO §8]`.

8. **El reparto de creacion NO sustituye nada de lo anterior.** Que Dali suba los creativos o que Romi maneje las paginas esta bien por division de trabajo y por rol minimo, pero NO es lo que protege. Lo que protege son los 7 puntos de arriba. Si alguien dice "ya estamos seguros porque repartimos quien crea que", esta equivocado `[CRITERIO, este es el punto central del documento]`.

---

## 7. Pasos concretos de setup de roles

### 7.1 Crear el Business Portfolio affiliate (Cris)
1. business.facebook.com > crear un nuevo Business Portfolio, dedicado al affiliate, con nombre de marca de salud y email de negocio de Cris. No reusar un portfolio de clientes `[BEST-PRACTICE Meta + CRITERIO aislamiento]`.
2. Activar 2FA y, si Meta lo ofrece, exigir 2FA a todos los miembros del portfolio (Business Settings > Security Center) `[BEST-PRACTICE Meta]`.

### 7.2 Invitar a Romi y Dali con el rol correcto (Cris, paso a paso)
1. Business Settings (Configuracion del negocio) > **People** (Personas) > **Add / Invite people**.
2. Ingresar el email de Romi (el ligado a SU cuenta de Facebook). Elegir nivel **Partial access** (acceso parcial), NO full control `[BEST-PRACTICE Meta]`.
3. Repetir para Dali con **Partial access**.
4. Ambos reciben invitacion por email y la aceptan desde SU propio dispositivo con SU 2FA.

### 7.3 Asignar activos y tasks por persona (Cris)
Despues de agregarlos al portfolio, asignar acceso por activo en Business Settings:
- **A Romi, sobre cada Pagina (y su IG):** Business Settings > Accounts > Pages > seleccionar la pagina > **Assign people** > Romi > activar tasks **Content**, **Community Activity**, **Insights** (dejar OFF Ads y dejar OFF el control total) `[BEST-PRACTICE Meta]`.
- **A Romi (opcional), sobre cada Ad Account:** Accounts > Ad accounts > seleccionar > Assign people > Romi > rol **Analyst** (solo View performance) `[BEST-PRACTICE Meta]`.
- **A Dali, sobre cada Ad Account:** Accounts > Ad accounts > seleccionar > Assign people > Dali > rol **Advertiser** (Manage campaigns + Manage creative + View performance; Manage account queda OFF) `[BEST-PRACTICE Meta]`.
- **Cris** se asigna a si mismo **Admin** en cada ad account y control total en paginas y datasets (suele venir por ser full control del portfolio, pero conviene verificarlo activo por activo) `[BEST-PRACTICE Meta]`.

Regla: asignar SIEMPRE por activo y por task, nunca dar "todo a todos". Meta misma recomienda dar solo el nivel que la persona necesita `[BEST-PRACTICE Meta]`.

### 7.4 Dar Partner Access por oferta (cuando aplique, futuro)
Solo cuando separes ofertas en portfolios distintos o quieras que el portfolio de agencia opere los activos:
1. En el portfolio DUENO de los activos: Business Settings > **Partners** > **Share assets with a partner** (o "Give a partner access to your assets").
2. Ingresar el **Business Portfolio ID** del portfolio operador (no un email personal). Seleccionar los activos y las tasks a compartir.
3. El portfolio operador maneja a su propia gente internamente. El dueno conserva la propiedad y puede revocar el acceso cuando quiera `[BEST-PRACTICE Meta]`.

### 7.5 Crear un System User para API (Cris, solo si hay automatizacion)
1. Business Settings > **Users** > **System Users** > **Add**.
2. Nombre del system user; rol **Employee** (no Admin, salvo necesidad real de acceso a todo el portfolio) `[BEST-PRACTICE Meta]`.
3. Click en el system user > **Assign assets** > seleccionar SOLO el/los ad account (y app) que la herramienta necesita, con la task minima `[BEST-PRACTICE Meta]`.
4. **Generate new token** > elegir la app y los permisos minimos (ej. ads_management) > copiar el token de inmediato (no se vuelve a mostrar) y guardarlo en `.env` local. Nunca en chat ni commits `[BEST-PRACTICE Meta + regla de seguridad OpenClaw]`.

---

## 8. Asignacion concreta para 3 ofertas

Quien administra que en cada stack, por oferta. (Ofertas/dominios ilustrativos del patron, no comprados.)

### Oferta 1 · DENTAL (ej. ProDentim)
| Activo | Crea | Owner/Admin | Acceso + rol exacto | Anti-ban |
|---|---|---|---|---|
| Dominio dailydentalfix.com | Cris | Cris | Cris | Verificado por DNS bajo el portfolio |
| Dataset 1 + CAPI | Cris | Cris | Cris (admin dataset) | Eventos solo oferta 1; validar compra $1 |
| Pagina FB + IG "Daily Dental Fix" | Cris | Portfolio | Romi (Content+Community+Insights) · Cris (admin) | Romi calienta la pagina antes de gastar |
| Tarjeta A | Cris | Cris | Solo Cris | Tarjeta unica de esta oferta |
| Ad Account 1 | Cris | Cris (Admin) | Dali (Advertiser) · Romi (Analyst opcional) | 1 nicho por cuenta |
| Campaign/Ad Set/Ads | Cris arma+publica; Dali crea/sube creativos | Cris | Dali (Manage creative/campaigns) | Disclaimer salud en cada ad; PAUSED hasta OK |

### Oferta 2 · IDIOMAS (ej. Rocket Languages)
| Activo | Crea | Owner/Admin | Acceso + rol exacto | Anti-ban |
|---|---|---|---|---|
| Dominio speakfasterguide.com | Cris | Cris | Cris | Verificado por DNS, dominio propio |
| Dataset 2 + CAPI | Cris | Cris | Cris | Eventos solo oferta 2 |
| Pagina FB + IG "Speak Faster" | Cris | Portfolio | Romi (Content+Community+Insights) · Cris (admin) | Warm-up propio, reloj nuevo |
| Tarjeta B | Cris | Cris | Solo Cris | Distinta de A y C |
| Ad Account 2 | Cris | Cris (Admin) | Dali (Advertiser) · Romi (Analyst opcional) | Aislado de oferta 1 y 3 |
| Campaign/Ad Set/Ads | Cris + Dali | Cris | Dali (Advertiser) | Idiomas no exige disclaimer salud, pero igual no copy-paste del vendor |

### Oferta 3 · WEIGHT LOSS (ej. Java Burn)
| Activo | Crea | Owner/Admin | Acceso + rol exacto | Anti-ban |
|---|---|---|---|---|
| Dominio morningmetabolic.com | Cris | Cris | Cris | Verificado por DNS |
| Dataset 3 + CAPI | Cris | Cris | Cris | Eventos solo oferta 3 |
| Pagina FB + IG "Morning Metabolic" | Cris | Portfolio | Romi (Content+Community+Insights) · Cris (admin) | Nicho de mayor vigilancia; warm-up cuidadoso |
| Tarjeta C | Cris | Cris | Solo Cris | Distinta de A y B |
| Ad Account 3 | Cris | Cris (Admin) | Dali (Advertiser) · Romi (Analyst opcional) | El stack mas sensible; aislado |
| Campaign/Ad Set/Ads | Cris + Dali | Cris | Dali (Advertiser) | Disclaimer "This product is not intended to diagnose, treat, cure, or prevent any disease" en el copy de CADA ad; cero claims tipo "pierde X kilos" |

**La regla de oro multi-oferta sigue vigente:** lanza de a UNA, no las tres a la vez. Con $2-5K el capital alcanza para un test serio `[FUENTE REPO §8 + 09-errores §5]`. Monta y valida la Oferta 1 completa (stack + warm-up de Romi + tracking validado por Cris + creativos de Dali). Cuando este estable, montas la 2. Recien con dos sanas, la 3. Cada stack arranca su propio reloj de warm-up.

---

*Documento interno OpenClaw / affiliate-business. `[FUENTE REPO]` = fuentes internas investigadas (estructura-bulletproof, 09-errores-foros) con cita; `[BEST-PRACTICE Meta]` = mecanica/estandar Meta Business 2025-2026 verificado en documentacion oficial y guias de la industria; `[CRITERIO]` = juicio operativo de este documento donde no hay dato exacto de fuente. Fuentes Meta verificadas: Meta Business Help Center (roles de ad account, partner access, system users), documentacion de Business Management APIs (system users y tokens), guias 2025-2026 (Leadsie, Graphed, AdAmigo, ChatArchitect, TJ21). Fuentes repo: `01-ejecucion-2026/meta-ads-estructura-bulletproof.md`, `00-viabilidad/research-fuentes/09-errores-foros-clickbank-meta.md`. La mecanica de Meta no se invento; lo no verificable se marca como criterio o se dice.*
