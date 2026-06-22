# Setup GitHub · Compartir con Romi y Dali

> Este archivo guía cómo poner el repo en GitHub privado y dar acceso a los 3 socios.
> Borrar este archivo después de hacer el setup.

---

## Pre-requisito · Cuentas GitHub de los 3

Antes de empezar, asegurarse que **Romi y Dali tienen cuenta GitHub** (gratis):
- github.com → Sign up
- Username sugerido: `romi-[apellido]`, `dali-[apellido]`
- Pasarles los usernames a Cris para invitar

---

## Camino A · Crear repo desde la web (más simple, sin instalar nada)

### 1. Crear el repo
1. Ir a https://github.com/new
2. **Repository name:** `affiliate-business`
3. **Description:** `Sistema operativo · Affiliate marketing performance · Equipo Romi/Cris/Dali`
4. **Visibility: Private** (crítico — nunca público)
5. **NO marcar** "Initialize with README" (ya tenemos)
6. Click "Create repository"

### 2. Conectar el repo local
GitHub te muestra los comandos. Ejecutar en terminal (**ya estás en la carpeta correcta**):

```bash
cd ~/Projects/affiliate-business
git remote add origin https://github.com/[TU-USUARIO]/affiliate-business.git
git branch -M main
git push -u origin main
```

(Reemplazar `[TU-USUARIO]` con tu username de GitHub)

### 3. Invitar a Romi y Dali
1. Ir al repo en github.com
2. **Settings** → **Collaborators** (panel izquierdo)
3. Click "Add people"
4. Buscar username de Romi → invitar como **Maintainer** (puede push directo)
5. Repetir para Dali

Romi y Dali recibirán email + notificación GitHub. Aceptan y ya están dentro.

### 4. Que Romi y Dali clonen el repo localmente
Cada uno en su laptop:
```bash
cd ~/Projects        # o donde quieran tener el repo
git clone https://github.com/[USUARIO-CRIS]/affiliate-business.git
cd affiliate-business
```

Si tienen Claude Code instalado:
```bash
claude
```

Y ya pueden trabajar — el `CLAUDE.md` se carga automático.

---

## Camino B · Con GitHub CLI (más rápido si tienes `gh` instalado)

### Si NO tienes `gh`:
```bash
brew install gh
gh auth login
```

### Crear repo + push en un solo comando:
```bash
cd ~/Projects/affiliate-business
gh repo create affiliate-business --private --source=. --description "Sistema operativo · Affiliate marketing · Equipo Romi/Cris/Dali" --push
```

### Invitar colaboradores:
```bash
gh api repos/[TU-USUARIO]/affiliate-business/collaborators/[USERNAME-ROMI] -X PUT -f permission=maintain
gh api repos/[TU-USUARIO]/affiliate-business/collaborators/[USERNAME-DALI] -X PUT -f permission=maintain
```

---

## Workflow Git para los 3 (Romi, Cris, Dali)

### Antes de empezar a trabajar (CRÍTICO)
```bash
cd ~/Projects/affiliate-business
git pull origin main
```

Sin pull antes, vas a tener conflicts cuando intentes push.

### Al terminar tu sesión
```bash
git add .
git commit -m "actualizar: [breve descripción]"
git push origin main
```

### Si hay conflict (Romi y Cris editaron mismo archivo)
- Git te dice qué archivo
- Abrir el archivo, ver los `<<<<<<<` y `>>>>>>>`
- Decidir qué versión queda
- `git add [archivo]` → `git commit` → `git push`

Si te complica, escribir en Slack #urgencias y Cris ayuda.

---

## Reglas de seguridad del repo

### NUNCA commitear
- `.env` (credenciales reales)
- API keys o tokens en código
- Datos personales de compradores
- Información de clientes OpenClaw (Cris, atención)
- Screenshots con números de cuenta

### Si commiteas algo sensible por error
1. **NO push** todavía si te das cuenta a tiempo
2. `git reset HEAD~1` (deshace el último commit local)
3. Borrar archivo sensible
4. Re-commit sin lo sensible

### Si ya hiciste push de algo sensible
1. Avisar inmediatamente al equipo en Slack
2. Cris ejecuta `git filter-branch` o usa BFG Repo-Cleaner
3. Rotar las credenciales expuestas (asumir que son públicas)

---

## .env · setup de cada uno

Cada miembro tiene su propio `.env` local (NUNCA en Git).

1. Copiar el template:
   ```bash
   cp .env.example .env
   ```

2. Editar `.env` con credenciales reales (cuando estén disponibles)

3. **Verificar que .env NO va a Git:**
   ```bash
   git status
   ```
   Si aparece `.env` en la lista → NO commitear, revisar `.gitignore`

---

## Branches (futuro · cuando quieran refinar)

Por ahora trabajamos directo en `main`. Cuando el equipo crezca o las cosas se compliquen:

- `feature/[descripción]` — para trabajo más largo
- `fix/[descripción]` — para correcciones
- PR review interno antes de merge a main

Decidir en retro mensual cuándo migrar a este flow.

---

## Troubleshooting común

### "Permission denied (publickey)" al hacer push
- Necesitas configurar SSH o usar HTTPS con token
- Más simple: usar HTTPS y GitHub te pedirá user/password (usar Personal Access Token, no contraseña)
- Crear token: github.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
- Permisos: `repo` (todo)

### "Updates were rejected"
- Hiciste cambios sin pull antes
- Solución: `git pull origin main --rebase`
- Resolver conflicts si hay
- `git push origin main`

### "Your branch is ahead of origin/main by X commits"
- Tienes cambios locales sin push
- Solución: `git push origin main`

---

## Después de hacer setup

**Borrar este archivo** (`SETUP-GITHUB.md`) — ya cumplió su propósito.

```bash
git rm SETUP-GITHUB.md
git commit -m "chore: eliminar guía setup github (ya configurado)"
git push origin main
```

---

*Guía válida hasta el primer push exitoso a GitHub.*
