# Multi-Project Context Management Task

## Purpose
Enable efficient management and switching between multiple project contexts while maintaining isolation and preventing cross-contamination.

## Behavioral Requirements
- **Example-Driven**: Reference patterns from past multi-project scenarios
- **Context Isolation**: Maintain strict separation between projects
- **Quick Switching**: Enable rapid context switches with zero friction
- **Memory Segregation**: Keep project-specific memories separate

## Multi-Project Architecture

### Context Organization Structure
```
.bmad/
├── active-project      # Symlink to current project
├── projects/
│   ├── project-a/
│   │   ├── context-state.md
│   │   ├── checkpoints/
│   │   ├── memories/
│   │   └── preferences.yml
│   ├── project-b/
│   │   ├── context-state.md
│   │   ├── checkpoints/
│   │   ├── memories/
│   │   └── preferences.yml
│   └── project-registry.yml
```

## Project Management Operations

### 1. Project Registration
When starting work on a new project:

```python
def register_project(project_name, project_path):
    """Register a new project in the multi-project system"""
    
    project_config = {
        "name": project_name,
        "path": project_path,
        "created": timestamp(),
        "last_accessed": timestamp(),
        "preferences": detect_project_preferences(project_path),
        "tech_stack": analyze_tech_stack(project_path),
        "team_size": estimate_team_size(project_path)
    }
    
    # Create project structure
    create_project_directories(project_name)
    
    # Initialize context
    initialize_project_context(project_name, project_config)
    
    # Update registry
    update_project_registry(project_name, project_config)
    
    return f"Project '{project_name}' registered successfully"
```

### 2. Project Listing
Show all registered projects with context:

```markdown
## 📁 Available Projects

### 1. **E-Commerce API** ⚡ (Active)
- **Path**: ~/projects/ecommerce-api
- **Last Active**: 2 hours ago
- **Status**: Feature development - Payment integration (65%)
- **Stack**: Node.js, PostgreSQL, Redis
- **Quick Switch**: `/project switch ecommerce-api`

### 2. **Analytics Dashboard**
- **Path**: ~/projects/analytics-dash
- **Last Active**: Yesterday at 4:30 PM
- **Status**: Bug fixing - Chart rendering issues
- **Stack**: React, TypeScript, D3.js
- **Quick Switch**: `/project switch analytics-dash`

### 3. **Mobile App**
- **Path**: ~/projects/mobile-app
- **Last Active**: 3 days ago
- **Status**: Planning - Push notification architecture
- **Stack**: React Native, Firebase
- **Quick Switch**: `/project switch mobile-app`

### Quick Commands
- `/project switch [name]` - Switch to project
- `/project status` - Current project details
- `/project list --detailed` - Full project information
```

### 3. Context Switching
Seamless switching between projects:

```python
def switch_project_context(target_project, save_current=True):
    """Switch to a different project context"""
    
    # Save current project state
    if save_current and has_active_project():
        auto_save_context(
            reason="Project switch",
            checkpoint_name=f"switch_to_{target_project}_{timestamp()}"
        )
    
    # Clear active context
    clear_active_context()
    
    # Load target project
    project_context = load_project_context(target_project)
    
    # Apply project-specific settings
    apply_project_preferences(project_context.preferences)
    
    # Restore project state
    restore_project_state(project_context)
    
    # Update active project indicator
    update_active_project(target_project)
    
    # Generate switch summary
    return generate_switch_summary(project_context)
```

#### Switch Summary Format
```markdown
## 🔄 Switched to: Analytics Dashboard

**Previous Project**: E-Commerce API (context saved)
**Time Since Last**: 18 hours ago

### 📊 Project State
- **Current Branch**: feature/chart-optimizations
- **Active Task**: Fixing D3.js memory leak in line charts
- **Progress**: Investigation phase (30%)

### 💡 Context Reminders
- You were debugging render performance
- Identified issue in data transformation loop
- Next step: Implement memoization strategy

### ⚡ Quick Actions
- `/continue` - Resume debugging
- `/test charts` - Run chart test suite
- `/review changes` - See what changed since yesterday
```

### 4. Cross-Project Insights
Leverage learnings across projects:

```markdown
## 🔗 Cross-Project Insights

### Similar Patterns Detected
Your **payment integration** in E-Commerce API is similar to:
- **Analytics Dashboard**: Stripe billing integration (6 months ago)
- **Previous Client**: Payment gateway setup (successful pattern)

### Reusable Solutions
1. **Webhook Security Pattern**
   - Used in 3 projects successfully
   - Ready-to-adapt code available
   - `/recall "webhook security pattern"`

2. **Error Handling Strategy**
   - Proven approach from Analytics Dashboard
   - Reduced support tickets by 60%
   - `/patterns error-handling`

### Team Overlaps
- **John**: Also working on Analytics Dashboard
- **Sarah**: Shared experience with payment systems
- Consider knowledge sharing session
```

### 5. Project Isolation Rules

#### Memory Isolation
```python
def query_project_memory(query, project_scope="current"):
    """Query memory with project isolation"""
    
    if project_scope == "current":
        # Only search current project's memories
        scope_filter = f"project:{get_active_project()}"
    elif project_scope == "all":
        # Search across all projects (with clear attribution)
        scope_filter = "project:*"
    elif project_scope == "related":
        # Search related projects (same tech stack/domain)
        scope_filter = build_related_projects_filter()
    
    results = search_memory(query, scope=scope_filter)
    
    # Always attribute memory source
    return attribute_memory_sources(results)
```

#### Preference Isolation
Each project maintains independent preferences:

```yaml
# project-a/preferences.yml
code_style:
  indent: 2
  quotes: single
  semicolons: false

ai_behavior:
  verbosity: concise
  example_preference: minimal
  quality_threshold: high

team_conventions:
  commit_format: conventional
  pr_template: enabled
  code_review: required
```

### 6. Project Context Branching
Create context variants within projects:

```markdown
## 🌿 Context Branching

### Current: feature/payment-integration

### Available Branches:
1. **main** (stable)
   - Last state: All tests passing
   - Clean working directory

2. **feature/payment-integration** ⚡ (active)
   - Current focus: Webhook implementation
   - 3 uncommitted changes

3. **experiment/graphql-migration**
   - Experimental: API restructuring
   - Isolated from main work

### Branch Operations:
- `/context branch create [name]` - New context branch
- `/context branch switch [name]` - Switch branches
- `/context branch merge [from]` - Merge contexts
- `/context branch delete [name]` - Remove branch
```

## Smart Project Detection

### Auto-Detection
Automatically detect project context:

```python
def auto_detect_project():
    """Automatically detect current project from cwd"""
    
    current_path = os.getcwd()
    
    # Check for project markers
    markers = [
        ".git",
        "package.json",
        "Cargo.toml",
        "pyproject.toml",
        ".bmad-project"
    ]
    
    project_root = find_project_root(current_path, markers)
    
    if project_root:
        # Check if registered
        if is_registered_project(project_root):
            return get_project_by_path(project_root)
        else:
            # Offer to register
            return prompt_project_registration(project_root)
    
    return None
```

### Smart Suggestions
Predict project switches:

```markdown
💡 **Project Switch Suggestion**

Based on your patterns:
- You typically switch to **Analytics Dashboard** on Mondays
- It's been 3 days since you checked **Mobile App**
- **Team Calendar**: Sprint review for E-Commerce API tomorrow

Would you like to switch projects?
```

## Project Templates

### Quick Project Setup
```markdown
## 🚀 Quick Project Setup

Detected new project: **customer-portal**
Tech stack identified: Next.js, TypeScript, Tailwind

### Would you like to:
1. Use **E-Commerce Template** (similar stack)
2. Use **Generic React Template**
3. Start fresh with custom setup
4. Import settings from existing project

Choose option (1-4):
```

## Error Handling

### Project Not Found
```markdown
❌ Project 'analytics' not found.

Did you mean:
- analytics-dashboard
- analytics-service
- data-analytics

Or `/project register analytics` to create new.
```

### Context Conflicts
```markdown
⚠️ Context Conflict Detected

**File**: src/api/handlers.js
**Conflict**: Different versions in contexts

Project A version: Newer (modified today)
Project B version: Older (3 days ago)

Resolution options:
1. Keep Project A version
2. Keep Project B version
3. Merge both versions
4. View diff first
```

## Integration Points

### Memory System
- Maintain project-specific memory namespaces
- Enable cross-project pattern recognition
- Track project-switching patterns

### Quality Framework
- Project-specific quality standards
- Consistent quality across context switches
- Prevent quality degradation during switches

### Behavioral Tracking
- Monitor multi-project productivity
- Identify optimal project-switching patterns
- Reduce context-switch overhead