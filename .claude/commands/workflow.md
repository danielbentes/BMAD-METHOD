# BMAD Workflow Management

Execute workflow operation: $ARGUMENTS

## Workflow Operations:
- **suggest** --context --confidence --alternatives: AI-powered next steps
- **handoff** [persona] --summary --checklist: Structured persona transition
- **core-dump** --format --include-memory: Save comprehensive session state
- **tasks** --category --recommended: List available tasks with insights
- **run-task** [task-name] [...args]: Execute specific BMAD task

## Workflow Requirements:
- **Context Preservation**: No information loss during transitions
- **Quality Continuity**: Maintain standards across workflow steps
- **Memory Integration**: Leverage and update system memory
- **Progressive Execution**: Break complex workflows into manageable steps

## Behavioral Compliance:
- All workflow operations use structured thinking
- Evidence-based recommendations only
- Example-driven approach for task execution
- Anti-pattern prevention throughout workflow

Parse workflow operation from $ARGUMENTS and execute with behavioral excellence.
