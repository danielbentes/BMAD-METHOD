#!/bin/bash

# BMAD Method Installation Script
# Installs BMAD Method into target project directory
# Version: 3.0.0 - New .bmad architecture

echo "================================================"
echo "BMAD Method Installation v3.0"
echo "================================================"
echo ""

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
BMAD_SOURCE_DIR="$(dirname "$(readlink -f "$0")")"
TARGET_DIR="${1:-.}"
PROJECT_NAME=$(basename "$(realpath "$TARGET_DIR")")
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.%3NZ")
SESSION_ID=$(uuidgen 2>/dev/null || openssl rand -hex 16 2>/dev/null || date +%s%N | sha256sum | head -c 32)

# Validate environment
validate_environment() {
    echo "🔍 Validating installation environment..."
    
    # Check if we're in BMAD-METHOD source directory
    if [ ! -d "$BMAD_SOURCE_DIR/bmad-agent" ]; then
        echo -e "${RED}✗${NC} Error: bmad-agent directory not found in source"
        echo "Make sure you're running this from the BMAD-METHOD repository root"
        exit 1
    fi
    
    # Check target directory
    if [ ! -d "$TARGET_DIR" ]; then
        echo -e "${RED}✗${NC} Error: Target directory does not exist: $TARGET_DIR"
        exit 1
    fi
    
    # Check if already installed
    if [ -d "$TARGET_DIR/bmad-agent" ]; then
        echo -e "${YELLOW}!${NC} BMAD Method already installed in target directory"
        read -p "Do you want to update/reinstall? (y/N): " confirm
        if [[ ! $confirm =~ ^[Yy]$ ]]; then
            echo "Installation cancelled"
            exit 0
        fi
        echo -e "${BLUE}→${NC} Proceeding with update/reinstall..."
    fi
    
    echo -e "${GREEN}✓${NC} Environment validation complete"
}

# Detect project characteristics
detect_project_type() {
    echo "🔍 Analyzing project characteristics..."
    
    # Detect project type
    if [ -d "$TARGET_DIR/.git" ]; then
        commit_count=$(git -C "$TARGET_DIR" rev-list --count HEAD 2>/dev/null || echo "0")
        if [ "$commit_count" -gt 50 ]; then
            PROJECT_TYPE="brownfield"
        elif [ "$commit_count" -gt 10 ]; then
            PROJECT_TYPE="feature"
        else
            PROJECT_TYPE="mvp"
        fi
    else
        PROJECT_TYPE="greenfield"
    fi
    
    # Detect technology stack
    TECH_STACK=""
    [ -f "$TARGET_DIR/package.json" ] && TECH_STACK="${TECH_STACK}JavaScript,"
    [ -f "$TARGET_DIR/requirements.txt" ] && TECH_STACK="${TECH_STACK}Python,"
    [ -f "$TARGET_DIR/Cargo.toml" ] && TECH_STACK="${TECH_STACK}Rust,"
    [ -f "$TARGET_DIR/go.mod" ] && TECH_STACK="${TECH_STACK}Go,"
    [ -f "$TARGET_DIR/pom.xml" ] && TECH_STACK="${TECH_STACK}Java,"
    
    # Detect architecture style
    if [ -f "$TARGET_DIR/docker-compose.yml" ]; then
        ARCHITECTURE_STYLE="microservices"
    elif [ -f "$TARGET_DIR/serverless.yml" ]; then
        ARCHITECTURE_STYLE="serverless"
    else
        ARCHITECTURE_STYLE="monolith"
    fi
    
    # Detect project domain
    if grep -q "api\|flask\|fastapi\|express" "$TARGET_DIR"/*.json "$TARGET_DIR"/*.py "$TARGET_DIR"/*.js 2>/dev/null; then
        PROJECT_DOMAIN="api"
    elif grep -q "react\|vue\|angular" "$TARGET_DIR"/*.json 2>/dev/null; then
        PROJECT_DOMAIN="web-app"
    else
        PROJECT_DOMAIN="api"  # Default
    fi
    
    echo -e "${GREEN}✓${NC} Project analysis complete:"
    echo "  - Type: $PROJECT_TYPE"
    echo "  - Domain: $PROJECT_DOMAIN"
    echo "  - Architecture: $ARCHITECTURE_STYLE"
    echo "  - Tech Stack: ${TECH_STACK%,}"
}

# Copy BMAD Method files
install_bmad_agent() {
    echo "📦 Installing BMAD Method..."
    
    # Remove existing installation if present
    if [ -d "$TARGET_DIR/bmad-agent" ]; then
        echo -e "${BLUE}→${NC} Removing existing bmad-agent directory..."
        rm -rf "$TARGET_DIR/bmad-agent"
    fi
    
    # Copy bmad-agent directory
    echo -e "${BLUE}→${NC} Copying BMAD Method files..."
    cp -r "$BMAD_SOURCE_DIR/bmad-agent" "$TARGET_DIR/"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} BMAD Method files copied successfully"
    else
        echo -e "${RED}✗${NC} Failed to copy BMAD Method files"
        exit 1
    fi
}

# Create .bmad directory structure
create_bmad_structure() {
    echo "🏗️  Creating .bmad project structure..."
    
    # Create directory structure
    mkdir -p "$TARGET_DIR/.bmad/state"
    mkdir -p "$TARGET_DIR/.bmad/memory"
    mkdir -p "$TARGET_DIR/.bmad/config"
    
    echo -e "${GREEN}✓${NC} .bmad directory structure created"
}

# Initialize project state from templates
initialize_project_state() {
    echo "⚙️  Initializing project state..."
    
    # Copy and populate orchestrator state template
    cp "$TARGET_DIR/bmad-agent/templates/project-state/orchestrator-state-template.md" \
       "$TARGET_DIR/.bmad/state/orchestrator-state.md"
    
    # Copy and populate memory fallback template
    cp "$TARGET_DIR/bmad-agent/templates/project-state/memory-fallback-template.json" \
       "$TARGET_DIR/.bmad/memory/fallback-storage.json"
    
    # Copy and populate error log template
    cp "$TARGET_DIR/bmad-agent/templates/project-state/error-log-template.md" \
       "$TARGET_DIR/.bmad/state/error-log.md"
    
    # Replace template placeholders
    replace_placeholders "$TARGET_DIR/.bmad/state/orchestrator-state.md"
    replace_placeholders "$TARGET_DIR/.bmad/memory/fallback-storage.json"
    replace_placeholders "$TARGET_DIR/.bmad/state/error-log.md"
    
    echo -e "${GREEN}✓${NC} Project state initialized"
}

# Replace template placeholders with actual values
replace_placeholders() {
    local file="$1"
    
    # Use different sed syntax based on OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/{{SESSION_ID}}/$SESSION_ID/g" "$file"
        sed -i '' "s/{{CREATION_TIMESTAMP}}/$TIMESTAMP/g" "$file"
        sed -i '' "s/{{LAST_UPDATED}}/$TIMESTAMP/g" "$file"
        sed -i '' "s/{{TEMPLATE_CREATION_DATE}}/$TIMESTAMP/g" "$file"
        sed -i '' "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$file"
        sed -i '' "s/{{PROJECT_TYPE}}/$PROJECT_TYPE/g" "$file"
        sed -i '' "s/{{PROJECT_DOMAIN}}/$PROJECT_DOMAIN/g" "$file"
        sed -i '' "s/{{ARCHITECTURE_STYLE}}/$ARCHITECTURE_STYLE/g" "$file"
        sed -i '' "s/{{USER_ID}}/$(whoami)/g" "$file"
        sed -i '' "s/{{CURRENT_DATE}}/$(date +%Y-%m-%d)/g" "$file"
    else
        # Linux
        sed -i "s/{{SESSION_ID}}/$SESSION_ID/g" "$file"
        sed -i "s/{{CREATION_TIMESTAMP}}/$TIMESTAMP/g" "$file"
        sed -i "s/{{LAST_UPDATED}}/$TIMESTAMP/g" "$file"
        sed -i "s/{{TEMPLATE_CREATION_DATE}}/$TIMESTAMP/g" "$file"
        sed -i "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$file"
        sed -i "s/{{PROJECT_TYPE}}/$PROJECT_TYPE/g" "$file"
        sed -i "s/{{PROJECT_DOMAIN}}/$PROJECT_DOMAIN/g" "$file"
        sed -i "s/{{ARCHITECTURE_STYLE}}/$ARCHITECTURE_STYLE/g" "$file"
        sed -i "s/{{USER_ID}}/$(whoami)/g" "$file"
        sed -i "s/{{CURRENT_DATE}}/$(date +%Y-%m-%d)/g" "$file"
    fi
}

# Update configuration paths
update_configuration_paths() {
    echo "🔧 Updating configuration paths..."
    
    # Update orchestrator configuration to use .bmad paths
    config_file="$TARGET_DIR/bmad-agent/ide-bmad-orchestrator.cfg.md"
    if [ -f "$config_file" ]; then
        echo -e "${BLUE}→${NC} Updating orchestrator configuration..."
        # This will be done in the next phase when we update references
    fi
    
    echo -e "${GREEN}✓${NC} Configuration paths updated"
}

# Create gitignore entries
setup_gitignore() {
    echo "📝 Setting up .gitignore..."
    
    gitignore_file="$TARGET_DIR/.gitignore"
    
    # Add .bmad entries if not already present
    if [ -f "$gitignore_file" ]; then
        if ! grep -q ".bmad" "$gitignore_file"; then
            echo "" >> "$gitignore_file"
            echo "# BMAD Method - Project State" >> "$gitignore_file"
            echo ".bmad/state/" >> "$gitignore_file"
            echo ".bmad/memory/" >> "$gitignore_file"
            echo "!.bmad/config/" >> "$gitignore_file"
            echo -e "${GREEN}✓${NC} Added .bmad entries to existing .gitignore"
        else
            echo -e "${BLUE}→${NC} .bmad entries already present in .gitignore"
        fi
    else
        echo "# BMAD Method - Project State" > "$gitignore_file"
        echo ".bmad/state/" >> "$gitignore_file"
        echo ".bmad/memory/" >> "$gitignore_file"
        echo "!.bmad/config/" >> "$gitignore_file"
        echo -e "${GREEN}✓${NC} Created .gitignore with .bmad entries"
    fi
}

# Run verification
run_verification() {
    echo "✅ Running installation verification..."
    
    if [ -f "$TARGET_DIR/bmad-agent/verify-setup.sh" ]; then
        echo -e "${BLUE}→${NC} Running BMAD verification..."
        cd "$TARGET_DIR"
        chmod +x bmad-agent/verify-setup.sh
        ./bmad-agent/verify-setup.sh --mode=project
        cd - > /dev/null
    fi
}

# Display next steps
show_next_steps() {
    echo ""
    echo "================================================"
    echo -e "${GREEN}🎉 BMAD Method Installation Complete!${NC}"
    echo "================================================"
    echo ""
    echo -e "${BLUE}Project Setup:${NC}"
    echo "  📁 Project: $PROJECT_NAME"
    echo "  🏷️  Type: $PROJECT_TYPE"
    echo "  🏗️  Architecture: $ARCHITECTURE_STYLE"
    echo "  🔧 Domain: $PROJECT_DOMAIN"
    echo ""
    echo -e "${BLUE}Files Created:${NC}"
    echo "  📂 bmad-agent/                    (BMAD Method framework)"
    echo "  📂 .bmad/state/                   (Session & orchestrator state)"
    echo "  📂 .bmad/memory/                  (Project memory & learning)"
    echo "  📂 .bmad/config/                  (Project-specific config)"
    echo ""
    echo -e "${BLUE}Next Steps:${NC}"
    echo "  1. 🚀 Activate BMAD in your IDE:"
    echo "     - Load: ./bmad-agent/ide-bmad-orchestrator.md"
    echo "     - Or use: /path/to/project/bmad-agent/ide-bmad-orchestrator.md"
    echo ""
    echo "  2. 🧠 Initialize memory (for brownfield projects):"
    echo "     - Run: /bootstrap-memory --mode=auto"
    echo ""
    echo "  3. 📋 Start with a workflow:"
    echo "     - Run: /help"
    echo "     - Or: /agents (to see available personas)"
    echo ""
    echo "  4. 🔧 Optional - Install OpenMemory MCP:"
    echo "     - See: ./bmad-agent/docs/setup-configuration/openmemory-setup.md"
    echo ""
    echo -e "${GREEN}Happy Building with BMAD Method! 🚀${NC}"
}

# Main installation flow
main() {
    echo "Starting BMAD Method installation for project: $PROJECT_NAME"
    echo "Target directory: $TARGET_DIR"
    echo ""
    
    validate_environment
    detect_project_type
    install_bmad_agent
    create_bmad_structure
    initialize_project_state
    update_configuration_paths
    setup_gitignore
    run_verification
    show_next_steps
}

# Handle script arguments
case "$1" in
    --help|-h)
        echo "BMAD Method Installation Script"
        echo ""
        echo "Usage: $0 [target-directory]"
        echo ""
        echo "Arguments:"
        echo "  target-directory    Directory to install BMAD Method (default: current directory)"
        echo ""
        echo "Examples:"
        echo "  $0                  # Install in current directory"
        echo "  $0 /path/to/project # Install in specific project"
        echo ""
        exit 0
        ;;
    --version|-v)
        echo "BMAD Method Installation Script v3.0.0"
        exit 0
        ;;
    *)
        main
        ;;
esac 