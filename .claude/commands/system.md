# BMAD System Management

Execute system operation: $ARGUMENTS

## System Operations:
- **init** --config --memory --force --minimal: Initialize BMAD orchestrator
- **status** --detailed --components --performance: Show system health
- **config** --validate --reload --backup --restore: Manage configuration
- **session** --save --restore --new --info: Manage session state
- **validate** --full --memory --personas --fix: Comprehensive validation

## System Management Framework:
- **Initialization Protocol**: Systematic startup with component validation
- **Health Monitoring**: Real-time status tracking with performance metrics
- **Configuration Management**: Safe configuration changes with rollback
- **Session Persistence**: Reliable state management across sessions
- **Validation Pipeline**: Comprehensive checks with automated recovery

## Core Components:
- **Configuration System**: Load and validate all BMAD configuration files
- **Memory Integration**: Establish connection to OpenMemory MCP if available
- **Persona System**: Verify all persona files are accessible and valid
- **Quality Framework**: Initialize behavioral enforcement and tracking
- **Session Management**: Maintain context and state across interactions

## Operational Excellence:
- **Proactive Monitoring**: Identify issues before they impact functionality
- **Automated Recovery**: Attempt safe fixes for common problems
- **Rollback Capabilities**: Enable undo for configuration changes
- **Performance Optimization**: Monitor and improve system performance
- **Security Compliance**: Ensure all operations follow security best practices

## Error Handling:
- Graceful degradation when components are unavailable
- Clear error reporting with specific remediation steps
- Automatic backup creation before risky operations
- Validation of all inputs and configurations

Execute system operation from $ARGUMENTS with operational excellence.
