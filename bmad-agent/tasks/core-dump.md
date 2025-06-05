# Core Dump Task

## CRITICAL SAFETY RULES - MANDATORY COMPLIANCE

### STOP CONDITIONS - ABORT IMMEDIATELY IF:
- User context contains sensitive data (passwords, API keys, secrets)
- Core dump would exceed 10KB size limit
- Previous core dump corruption detected
- Memory system reports integrity issues
- User explicitly requested no persistence

### MANDATORY VALIDATIONS BEFORE PROCEEDING:
1. **Privacy Check**: Scan for PII, credentials, or sensitive data
2. **Size Projection**: Estimate final file size before creation
3. **Integrity Verification**: Validate existing core dumps if present
4. **Permission Confirmation**: Verify user consent for persistence
5. **System State**: Confirm memory system health status

### QUALITY GATES - MUST PASS ALL:
- [ ] No sensitive data detected in context
- [ ] File size projection under 10KB
- [ ] User consent confirmed or implied
- [ ] Memory system operational
- [ ] Write permissions available

## Purpose

To create a concise memory recording file (`.bmad/system/core-dumps/core-dump-n.md`) that captures the essential context of the current agent session, enabling seamless continuation of work in future agent sessions. This task ensures persistent context across agent conversations while maintaining minimal token usage for efficient context loading.

## Progressive Disclosure Phases

### Phase 1: Safety Assessment (MANDATORY)
1. Scan context for sensitive data patterns
2. Check existing core dump integrity
3. Validate system permissions
4. Estimate content size
5. **GATE**: All safety checks passed → Continue to Phase 2

### Phase 2: Content Analysis
1. Identify key accomplishments
2. Extract critical decisions
3. Document file changes
4. Capture user preferences
5. **GATE**: Meaningful content identified → Continue to Phase 3

### Phase 3: Core Dump Creation with Context Preservation
1. Structure content for minimal tokens
2. Apply compression strategies
3. Create automatic context checkpoint
4. Validate completeness
5. Write to persistent storage
6. Update context restoration indices
7. **GATE**: File created successfully → Continue to Phase 4

### Phase 4: Verification
1. Read back created file
2. Verify content integrity
3. Check file permissions
4. Update memory indices
5. **FINAL GATE**: All verifications passed → Task Complete

## Inputs for this Task

### Required Inputs (MUST HAVE ALL):
- Current session conversation history and accomplishments
- Files created, modified, or deleted during the session
- Key decisions made and procedures followed
- Current project state and next logical steps
- User requests and agent responses that shaped the session

### Validation Requirements:
- **Context History**: Must be complete and uncorrupted
- **File Changes**: Must have accurate before/after states
- **Decision Log**: Must include rationale and context
- **Project State**: Must reflect actual current conditions
- **User Interactions**: Must preserve intent and preferences

## Task Execution Instructions

### 0. Pre-Execution Safety Protocol

#### Existing Core Dump Check
Before proceeding, check if `.bmad/system/core-dumps/core-dump-1.md` already exists:

##### If File Exists:
1. **Integrity Check**: Validate existing file structure and content
2. **Backup Creation**: Create `.bmad/system/core-dumps/backup/core-dump-1.bak`
3. **User Query**: "Core dump file exists. Should I: 1. Overwrite, 2. Update, 3. Append or 4. Create new?"
   - **Overwrite**: Replace entire file with new content (after backup)
   - **Update**: Merge new context info with existing content, updating relevant sections
   - **Append**: Add new context as a separate entry while preserving existing content
   - **Create New**: Create next sequential file (e.g., core-dump-2.md)
4. **Confirmation**: Require explicit user confirmation for destructive operations

##### If File Doesn't Exist:
1. **Directory Check**: Ensure `.bmad/system/core-dumps/` directory exists
2. **Permission Test**: Verify write permissions
3. **Space Check**: Confirm adequate disk space
4. **Proceed**: Create `.bmad/system/core-dumps/core-dump-1.md`

#### Error Conditions:
- **Corrupted File**: Alert user, offer recovery options
- **Permission Denied**: Provide troubleshooting steps
- **Disk Full**: Calculate required space, suggest cleanup
- **Invalid Path**: Create directory structure if missing

### 1. Analyze Current Context

- Review the entire conversation to identify key accomplishments
- Note any specific tasks, procedures, or workflows that were executed
- Identify important decisions made or problems solved
- Capture the user's working style and preferences observed during the session

### 2. Document What Was Accomplished

- **Primary Actions**: List the main tasks completed concisely
- **Story Progress**: For story work, use format "Tasks Complete: 1-6, 8. Next Task Pending: 7, 9"
- **Problem Solving**: Document any challenges encountered and how they were resolved
- **User Communications**: Summarize key user requests, preferences, and discussion points

### 3. Record File System Changes (Concise Format)

- **Files Created**: `filename.ext` (brief purpose/size)
- **Files Modified**: `filename.ext` (what changed)
- **Files Deleted**: `filename.ext` (why removed)
- Focus on essential details, avoid verbose descriptions

### 4. Capture Current Project State

- **Project Progress**: Where the project stands after this context
- **Current Issues**: Any blockers or problems that need resolution
- **Next Logical Steps**: What would be the natural next actions to take

### 5. Create/Update Core Dump File

Based on user's choice from step 0, handle the file accordingly:

### 6. Optimize for Minimal Context

- Keep descriptions concise but informative
- Use abbreviated formats where possible (file sizes, task numbers)
- Focus on actionable information rather than detailed explanations
- Avoid redundant information that can be found in project documentation
- Prioritize information that would be lost without this recording
- Ensure the file can be quickly scanned and understood

### 7. Validate Completeness

#### Content Validation Checklist:
- [ ] All significant session activities captured
- [ ] Future agent can understand current state
- [ ] File changes accurately recorded with paths
- [ ] Next steps clear and actionable
- [ ] User preferences and style documented
- [ ] No sensitive data included
- [ ] File size within limits (<10KB)
- [ ] Timestamps accurate and consistent

#### Quality Metrics:
- **Completeness Score**: Must be ≥90%
- **Clarity Rating**: Must be "High" or "Very High"
- **Token Efficiency**: Must use <2000 tokens when loaded
- **Recovery Potential**: Must enable full context restoration

### 8. Error Recovery Procedures

#### Common Failure Scenarios:

1. **Write Permission Denied**
   - Attempt alternate location: `.bmad/temp/core-dump-emergency.md`
   - Provide manual copy instructions
   - Suggest permission fix commands

2. **File Size Exceeded**
   - Apply aggressive summarization
   - Split into multiple files if necessary
   - Prioritize most recent/critical information

3. **Corruption During Write**
   - Restore from backup
   - Retry with atomic write operation
   - Fall back to append mode

4. **Sensitive Data Detected**
   - Abort write operation
   - Report specific patterns found
   - Offer sanitized version option

### 9. Success Metrics

#### Immediate Metrics:
- Core dump created successfully
- File size optimized (<10KB)
- No sensitive data included
- All phases completed without errors

#### Long-term Metrics:
- Successful context restorations: >95%
- Average load time: <2 seconds
- User satisfaction with continuity: >90%
- Zero security incidents from dumps

### 10. Context Preservation Integration

#### Automatic Context Checkpoint:
When creating core dump, simultaneously:
1. Create timestamped context checkpoint
2. Update `.bmad/state/context-state.md` 
3. Tag with "core-dump" for easy retrieval
4. Link to memory system for enhanced recall

#### Smart Restoration Linkage:
- Core dumps automatically indexed for context restoration
- Quick restore command: `/context restore core-dump-{n}`
- Memory system notified of significant state capture
- Enables "what's changed" analysis from this point

#### Context Continuity Features:
- Auto-detect if user is leaving (farewell phrases)
- Create "end-of-session" summary in addition to core dump
- Prepare "welcome back" briefing for next session
- Track time gaps for intelligent restoration

### 11. Continuous Improvement

#### Post-Execution Analysis:
1. Log execution time and file size
2. Track any errors or warnings
3. Note user feedback on format
4. Identify optimization opportunities

#### Feedback Integration:
- Regular review of core dump effectiveness
- User surveys on context restoration quality
- Performance metrics analysis
- Security audit results

#### Update Triggers:
- New sensitive data patterns identified
- Performance degradation detected
- User feedback indicates issues
- Security vulnerabilities discovered
