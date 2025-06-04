# BMAD Method Architecture Migration v3.0

## Migration Overview

The BMAD Method has undergone a significant architectural restructuring to separate **method definition** from **project usage**, implementing proper separation of concerns and enabling clean deployments to target projects.

## Architecture Changes

### v2.x Architecture (Legacy)
```
project-root/
  .ai/                          # ❌ Mixed method + project data
    orchestrator-state.md       # Project-specific state
    memory-fallback.json        # Project-specific memory
    memory_integration_wrapper.py # Method infrastructure
    populate-orchestrator-state.py # Method infrastructure
    error-log.md               # Project-specific errors
```

### v3.0 Architecture (Current)
```
# Method Repository (BMAD-METHOD)
bmad-agent/                    # ✅ Method definition only
  data/memory-system/          # Memory infrastructure
    memory_integration_wrapper.py
    memory-sync-integration.py
    orchestrator-state-schema.yml
    populate-orchestrator-state.py
    validate-orchestrator-state.py
  templates/project-state/     # Clean templates
    orchestrator-state-template.md
    memory-fallback-template.json
    error-log-template.md
  commands/                    # Command definitions
  personas/                    # Persona definitions
  tasks/                       # Task definitions
  [...other method components]

# Target Project (After Installation)
project-root/
  bmad-agent/                  # Copied method framework
  .bmad/                       # ✅ Project-specific data only
    state/                     # Session & orchestrator state
      orchestrator-state.md
      error-log.md
    memory/                    # Project memory & learning
      fallback-storage.json
    config/                    # Project-specific config
```

## Key Architectural Principles

### 1. **Separation of Concerns**
- **Method Definition**: Lives in `bmad-agent/` (versioned, shared)
- **Project Instance**: Lives in `.bmad/` (gitignored, project-specific)
- **Clear Boundaries**: No mixing of method infrastructure with project data

### 2. **Clean Deployment**
- **Installation Script**: `install-bmad.sh` deploys method to target projects
- **Template System**: Clean templates with placeholders for project initialization
- **Auto-Detection**: Analyzes target project characteristics and adapts

### 3. **State Management Evolution**
- **Orchestrator State**: `.bmad/state/orchestrator-state.md` (project session)
- **Memory Storage**: `.bmad/memory/fallback-storage.json` (project learning)
- **Error Logging**: `.bmad/state/error-log.md` (project diagnostics)

### 4. **Path Migration Strategy**
All internal references updated:
- `.ai/orchestrator-state.md` → `.bmad/state/orchestrator-state.md`
- `.ai/memory-fallback.json` → `.bmad/memory/fallback-storage.json`
- `.ai/error-log.md` → `.bmad/state/error-log.md`

## Installation Process

### For New Projects
```bash
# From BMAD-METHOD repository
./install-bmad.sh /path/to/target/project

# Result: Clean BMAD installation with project-specific initialization
```

### For Existing Projects (Migration)
```bash
# 1. Backup existing .ai directory
cp -r .ai .ai.backup.$(date +%Y%m%d)

# 2. Install BMAD
/path/to/BMAD-METHOD/install-bmad.sh .

# 3. Migrate existing state (if needed)
cp .ai.backup/orchestrator-state.md .bmad/state/
cp .ai.backup/memory-fallback.json .bmad/memory/fallback-storage.json

# 4. Remove old structure
rm -rf .ai/
```

## Benefits of New Architecture

### ✅ **Developer Experience**
- **Clear Installation**: Single script deploys BMAD to any project
- **Project Isolation**: Each project has independent BMAD state
- **Clean Git History**: Project state excluded from version control
- **Easy Updates**: Method updates don't affect project state

### ✅ **Operational Excellence**
- **Proper Separation**: Method vs. usage clearly delineated
- **Template System**: Consistent initialization across projects
- **Path Consistency**: All references use new `.bmad` structure
- **Migration Support**: Smooth transition from legacy structure

### ✅ **Team Collaboration**
- **Shared Method**: Common BMAD version across team projects
- **Individual State**: Each developer's session state isolated
- **Configuration Control**: Team config in `.bmad/config/` can be versioned
- **Memory Privacy**: Personal learning stays private in `.bmad/memory/`

## Directory Purpose Guide

### `bmad-agent/` (Method Framework)
- **Purpose**: Core BMAD Method definition and infrastructure
- **Contents**: Personas, tasks, commands, memory system, templates
- **Versioning**: Tracked in git, shared across projects
- **Updates**: Updated by pulling latest BMAD Method version

### `.bmad/state/` (Session State)
- **Purpose**: Current session and orchestrator state
- **Contents**: `orchestrator-state.md`, `error-log.md`
- **Versioning**: Gitignored, not shared
- **Lifecycle**: Created/updated during BMAD sessions

### `.bmad/memory/` (Learning & Memory)
- **Purpose**: Project-specific learning and memory accumulation
- **Contents**: `fallback-storage.json`, memory patterns
- **Versioning**: Gitignored, personal to developer
- **Lifecycle**: Grows over time as BMAD learns project patterns

### `.bmad/config/` (Project Configuration)
- **Purpose**: Project-specific BMAD configuration
- **Contents**: Custom settings, team preferences
- **Versioning**: Tracked in git, shared with team
- **Lifecycle**: Set once, updated as team preferences evolve

## Migration Validation

### Verification Commands
```bash
# Verify new structure exists
ls -la .bmad/

# Check orchestrator state
head .bmad/state/orchestrator-state.md

# Validate memory storage
cat .bmad/memory/fallback-storage.json | jq .

# Test memory system scripts
python bmad-agent/data/memory-system/validate-orchestrator-state.py

# Run full validation
bmad-agent/verify-setup.sh --mode=project
```

### Success Criteria
- ✅ `.bmad/` directory structure created
- ✅ Project state files initialized with correct placeholders
- ✅ Memory system references updated to new paths
- ✅ Gitignore properly excludes state/memory, allows config
- ✅ Installation script works on fresh projects
- ✅ All memory system scripts use new paths

## Rollback Strategy

### Emergency Rollback
```bash
# 1. Restore from backup
cp -r .ai.backup.* .ai/

# 2. Remove new structure
rm -rf .bmad/

# 3. Update bmad-agent references (if needed)
git checkout HEAD~1 bmad-agent/

# 4. Clean gitignore
sed -i '/\.bmad/d' .gitignore
```

### Gradual Migration
```bash
# Keep both structures temporarily
# Old: .ai/ (legacy, read-only)
# New: .bmad/ (active)
# Remove .ai/ after validation period
```

## Future Considerations

### v3.1 Enhancements
- **Config Templates**: Standardized project configuration templates
- **Team Synchronization**: Shared config and learning patterns
- **Cloud Integration**: Optional cloud-based memory synchronization
- **Multi-Project Learning**: Cross-project pattern recognition

### Best Practices
- **Installation**: Always use `install-bmad.sh` for new projects
- **Updates**: Keep `bmad-agent/` updated, preserve `.bmad/` state
- **Backup**: Regular backups of `.bmad/memory/` for valuable learning
- **Team Coordination**: Share `.bmad/config/` for team alignment

---

**Migration Date**: 2025-06-04  
**Architecture Version**: 3.0  
**Status**: ✅ Complete  
**Next Review**: 2025-07-04 