# {Project Name} Frontend Architecture Document

## Table of Contents

{ Update this if sections and subsections are added or removed }

- [Introduction](#introduction)
- [Overall Frontend Philosophy & Patterns](#overall-frontend-philosophy--patterns)
- [Design System Compliance & Tracking](#design-system-compliance--tracking)
  - [Design System Foundation](#design-system-foundation)
  - [Design Token Management](#design-token-management)
  - [Component Compliance Tracking](#component-compliance-tracking)
  - [Design Review Process](#design-review-process)
- [Detailed Frontend Directory Structure](#detailed-frontend-directory-structure)
- [Component Breakdown & Implementation Details](#component-breakdown--implementation-details)
  - [Component Naming & Organization](#component-naming--organization)
  - [Component Reusability Metrics](#component-reusability-metrics)
  - [Template for Component Specification](#template-for-component-specification)
- [State Management In-Depth](#state-management-in-depth)
  - [Store Structure / Slices](#store-structure--slices)
  - [Key Selectors](#key-selectors)
  - [Key Actions / Reducers / Thunks](#key-actions--reducers--thunks)
- [API Interaction Layer](#api-interaction-layer)
  - [Client/Service Structure](#clientservice-structure)
  - [Error Handling & Retries (Frontend)](#error-handling--retries-frontend)
- [Routing Strategy](#routing-strategy)
  - [Route Definitions](#route-definitions)
  - [Route Guards / Protection](#route-guards--protection)
- [Build, Bundling, and Deployment](#build-bundling-and-deployment)
  - [Build Process & Scripts](#build-process--scripts)
  - [Key Bundling Optimizations](#key-bundling-optimizations)
  - [Deployment to CDN/Hosting](#deployment-to-cdnhosting)
- [Frontend Testing Strategy](#frontend-testing-strategy)
  - [Component Testing](#component-testing)
  - [UI Integration/Flow Testing](#ui-integrationflow-testing)
  - [End-to-End UI Testing Tools & Scope](#end-to-end-ui-testing-tools--scope)
- [Accessibility (AX) Implementation Details](#accessibility-ax-implementation-details)
  - [Accessibility Standards & Compliance](#accessibility-standards--compliance)
  - [Implementation Requirements](#implementation-requirements)
  - [Accessibility Validation Framework](#accessibility-validation-framework)
  - [Component-Level Accessibility Requirements](#component-level-accessibility-requirements)
  - [Accessibility Evidence Collection](#accessibility-evidence-collection)
- [Performance Considerations](#performance-considerations)
  - [Performance Benchmarks & Evidence Requirements](#performance-benchmarks--evidence-requirements)
  - [Performance Optimization Strategies](#performance-optimization-strategies)
  - [Performance Monitoring & Tracking](#performance-monitoring--tracking)
- [Internationalization (i18n) and Localization (l10n) Strategy](#internationalization-i18n-and-localization-l10n-strategy)
- [Feature Flag Management](#feature-flag-management)
- [Frontend Security Considerations](#frontend-security-considerations)
- [User Experience Validation Requirements](#user-experience-validation-requirements)
  - [UX Metrics & Targets](#ux-metrics--targets)
  - [User Flow Validation](#user-flow-validation)
  - [Analytics & Monitoring](#analytics--monitoring)
- [Responsive Design Evidence & Requirements](#responsive-design-evidence--requirements)
  - [Device & Viewport Coverage](#device--viewport-coverage)
  - [Responsive Testing Requirements](#responsive-testing-requirements)
  - [Adaptive Features](#adaptive-features)
  - [Evidence Collection](#evidence-collection)
- [Browser Support and Progressive Enhancement](#browser-support-and-progressive-enhancement)
- [Change Log](#change-log)

## Introduction

{ This document details the technical architecture specifically for the frontend of {Project Name}. It complements the main {Project Name} Architecture Document and the UI/UX Specification. This document details the frontend architecture and **builds upon the foundational decisions** (e.g., overall tech stack, CI/CD, primary testing tools) defined in the main {Project Name} Architecture Document (`docs/architecture.md` or linked equivalent). **Frontend-specific elaborations or deviations from general patterns must be explicitly noted here.** The goal is to provide a clear blueprint for frontend development, ensuring consistency, maintainability, and alignment with the overall system design and user experience goals. }

- **Link to Main Architecture Document (REQUIRED):** {e.g., `docs/architecture.md`}
- **Link to UI/UX Specification (REQUIRED if exists):** {e.g., `docs/front-end-spec.md`}
- **Link to Primary Design Files (Figma, Sketch, etc.) (REQUIRED if exists):** {From UI/UX Spec}
- **Link to Deployed Storybook / Component Showcase (if applicable):** {URL}

## Overall Frontend Philosophy & Patterns

{ Describe the core architectural decisions and patterns chosen for the frontend. This should align with the "Definitive Tech Stack Selections" in the main architecture document and consider implications from the overall system architecture (e.g., monorepo vs. polyrepo, backend service structure). }

- **Framework & Core Libraries:** {e.g., React 18.x with Next.js 13.x, Angular 16.x, Vue 3.x with Nuxt.js}. **These are derived from the 'Definitive Tech Stack Selections' in the main Architecture Document.** This section elaborates on *how* these choices are applied specifically to the frontend.
- **Component Architecture:** {e.g., Atomic Design principles, Presentational vs. Container components, use of specific component libraries like Material UI, Tailwind CSS for styling approach. Specify chosen approach and any key libraries.}
- **State Management Strategy:** {e.g., Redux Toolkit, Zustand, Vuex, NgRx. Briefly describe the overall approach – global store, feature stores, context API usage. **Referenced from main Architecture Document and detailed further in "State Management In-Depth" section.**}
- **Data Flow:** {e.g., Unidirectional data flow (Flux/Redux pattern), React Query/SWR for server state. Describe how data is fetched, cached, passed to components, and updated.}
- **Styling Approach:** **{Chosen Styling Solution, e.g., Tailwind CSS / CSS Modules / Styled Components}**. Configuration File(s): {e.g., `tailwind.config.js`, `postcss.config.js`}. Key conventions: {e.g., "Utility-first approach for Tailwind. Custom components defined in `src/styles/components.css`. Theme extensions in `tailwind.config.js` under `theme.extend`. For CSS Modules, files are co-located with components, e.g., `MyComponent.module.css`.}
- **Key Design Patterns Used:** {e.g., Provider pattern, Hooks, Higher-Order Components, Service patterns for API calls, Container/Presentational. These patterns are to be consistently applied. Deviations require justification and documentation.}

## Design System Compliance & Tracking

{ Define how the application adheres to design system standards and tracks compliance with evidence requirements. }

### Design System Foundation

- **Design System Source:** {e.g., Custom design system, Material Design, Ant Design, Bootstrap}
- **Design Tokens Location:** {e.g., `src/design-system/tokens.ts` or design tool API}
- **Component Library:** {e.g., Internal component library, Storybook instance URL}

### Design Token Management

- **Token Categories & Evidence:**
  | Token Type | Source of Truth | Implementation | Validation Method |
  | :--- | :--- | :--- | :--- |
  | Colors | {e.g., Figma variables} | CSS variables/JS constants | Visual regression tests |
  | Typography | Design system docs | Typography config file | Computed styles audit |
  | Spacing | 8px grid system | Spacing scale utilities | Layout analysis tools |
  | Breakpoints | Responsive guidelines | Media query constants | Cross-device testing |
  | Shadows | Elevation system | Shadow utilities | Visual comparison |
  | Animation | Motion guidelines | Transition presets | Performance profiling |

### Component Compliance Tracking

- **Compliance Metrics:**
  | Metric | Target | Evidence Required | Tool |
  | :--- | :--- | :--- | :--- |
  | Design Token Usage | 100% | No hardcoded values audit | ESLint rules |
  | Component Alignment | 95% | Visual regression report | Percy/Chromatic |
  | Spacing Consistency | 100% | Grid alignment check | Layout Inspector |
  | Color Contrast | WCAG AA | Contrast analysis report | Automated tooling |
  | Typography Scale | 100% | Font usage audit | CSS analysis |

- **Visual Regression Testing:**
  - Tool: {e.g., Percy, Chromatic, Loki}
  - Baseline: Design system reference components
  - Threshold: < 0.1% visual difference allowed
  - Review Process: Design team approval for any deviations

### Design Review Process

- **Component Design Review Checklist:**
  - [ ] Uses only approved design tokens
  - [ ] Matches Figma/Sketch specifications exactly
  - [ ] Responsive behavior documented and tested
  - [ ] Micro-interactions follow motion guidelines
  - [ ] States (hover, focus, active, disabled) defined
  - [ ] Dark mode variant implemented (if applicable)
  - [ ] Design team approval obtained

- **Evidence Collection:**
  | Review Type | Artifacts Required | Storage Location |
  | :--- | :--- | :--- |
  | Initial Design | Figma links, specs | `.design/components/` |
  | Implementation | Screenshots, code | `.design/implementation/` |
  | Visual Testing | Regression reports | `.design/visual-tests/` |
  | Design Approval | Sign-off documents | `.design/approvals/` |

## Detailed Frontend Directory Structure

{ Provide an ASCII diagram representing the frontend application\'s specific folder structure (e.g., within `src/` or `app/` or a dedicated `frontend/` root directory if part of a monorepo). This should elaborate on the frontend part of the main project structure outlined in the architecture document. Highlight conventions for organizing components, pages/views, services, state, styles, assets, etc. For each key directory, provide a one-sentence mandatory description of its purpose.}

### EXAMPLE - Not Prescriptive (for a React/Next.js app)

```plaintext
src/
├── app/                        # Next.js App Router: Pages/Layouts/Routes. MUST contain route segments, layouts, and page components.
│   ├── (features)/             # Feature-based routing groups. MUST group related routes for a specific feature.
│   │   └── dashboard/
│   │       ├── layout.tsx      # Layout specific to the dashboard feature routes.
│   │       └── page.tsx        # Entry page component for a dashboard route.
│   ├── api/                    # API Routes (if using Next.js backend features). MUST contain backend handlers for client-side calls.
│   ├── globals.css             # Global styles. MUST contain base styles, CSS variable definitions, Tailwind base/components/utilities.
│   └── layout.tsx              # Root layout for the entire application.
├── components/                 # Shared/Reusable UI Components.
│   ├── ui/                     # Base UI elements (Button, Input, Card). MUST contain only generic, reusable, presentational UI elements, often mapped from a design system. MUST NOT contain business logic.
│   │   ├── Button.tsx
│   │   └── ...
│   ├── layout/                 # Layout components (Header, Footer, Sidebar). MUST contain components structuring page layouts, not specific page content.
│   │   ├── Header.tsx
│   │   └── ...
│   └── (feature-specific)/     # Components specific to a feature but potentially reusable within it. This is an alternative to co-locating within features/ directory.
│       └── user-profile/
│           └── ProfileCard.tsx
├── features/                   # Feature-specific logic, hooks, non-global state, services, and components solely used by that feature.
│   └── auth/
│       ├── components/         # Components used exclusively by the auth feature. MUST NOT be imported by other features.
│       ├── hooks/              # Custom React Hooks specific to the 'auth' feature. Hooks reusable across features belong in `src/hooks/`.
│       ├── services/           # Feature-specific API interactions or orchestrations for the 'auth' feature.
│       └── store.ts            # Feature-specific state slice (e.g., Redux slice) if not part of a global store or if local state is complex.
├── hooks/                      # Global/sharable custom React Hooks. MUST be generic and usable by multiple features/components.
│   └── useAuth.ts
├── lib/ / utils/             # Utility functions, helpers, constants. MUST contain pure functions and constants, no side effects or framework-specific code unless clearly named (e.g., `react-helpers.ts`).
│   └── utils.ts
├── services/                   # Global API service clients or SDK configurations. MUST define base API client instances and core data fetching/mutation services.
│   └── apiClient.ts
├── store/                      # Global state management setup (e.g., Redux store, Zustand store).
│   ├── index.ts                # Main store configuration and export.
│   ├── rootReducer.ts          # Root reducer if using Redux.
│   └── (slices)/               # Directory for global state slices (if not co-located in features).
├── styles/                     # Global styles, theme configurations (if not using `globals.css` or similar, or for specific styling systems like SCSS partials).
└── types/                      # Global TypeScript type definitions/interfaces. MUST contain types shared across multiple features/modules.
    └── index.ts
```

### Notes on Frontend Structure:

{ Explain any specific conventions or rationale behind the structure. e.g., "Components are co-located with their feature if not globally reusable to improve modularity." AI Agent MUST adhere to this defined structure strictly. New files MUST be placed in the appropriate directory based on these descriptions. }

## Component Breakdown & Implementation Details

{ This section outlines the conventions and templates for defining UI components. Detailed specification for most feature-specific components will emerge as user stories are implemented. The AI agent MUST follow the "Template for Component Specification" below whenever a new component is identified for development. }

### Component Naming & Organization

- **Component Naming Convention:** **{e.g., PascalCase for files and component names: `UserProfileCard.tsx`}**. All component files MUST follow this convention.
- **Organization:** {e.g., "Globally reusable components in `src/components/ui/` or `src/components/layout/`. Feature-specific components co-located within their feature directory, e.g., `src/features/feature-name/components/`. Refer to Detailed Frontend Directory Structure.}

### Component Reusability Metrics

- **Reusability Classification:**
  | Category | Definition | Location | Reuse Target |
  | :--- | :--- | :--- | :--- |
  | Atomic | Basic UI elements (buttons, inputs) | `src/components/ui/` | > 10 instances |
  | Molecular | Composite components | `src/components/shared/` | > 5 instances |
  | Organism | Complex feature components | `src/components/features/` | > 3 instances |
  | Template | Page layouts | `src/components/layouts/` | > 2 instances |
  | Feature-specific | Single-use components | `src/features/*/components/` | 1 instance |

- **Reusability Evidence Requirements:**
  - [ ] Component usage tracking via static analysis
  - [ ] Prop interface documentation completeness
  - [ ] Storybook coverage for all reusable components
  - [ ] Generic vs specific prop ratio > 80%
  - [ ] No hardcoded values or business logic in reusable components

- **Component Quality Metrics:**
  | Metric | Target | Measurement Method |
  | :--- | :--- | :--- |
  | Prop Type Coverage | 100% | TypeScript strict mode |
  | Storybook Stories | 100% for shared | Story count analysis |
  | Unit Test Coverage | > 90% | Jest coverage reports |
  | Accessibility Score | 100% | jest-axe automation |
  | Bundle Size Impact | < 20KB | Webpack analysis |

### Template for Component Specification

{ For each significant UI component identified from the UI/UX Specification and design files (Figma), the following details MUST be provided. Repeat this subsection for each component. The level of detail MUST be sufficient for an AI agent or developer to implement it with minimal ambiguity. }

#### Component: `{ComponentName}` (e.g., `UserProfileCard`, `ProductDetailsView`)

- **Purpose:** {Briefly describe what this component does and its role in the UI. MUST be clear and concise.}
- **Source File(s):** {e.g., `src/components/user-profile/UserProfileCard.tsx`. MUST be the exact path.}
- **Visual Reference:** {Link to specific Figma frame/component, or Storybook page. REQUIRED.}
- **Props (Properties):**
  { List each prop the component accepts. For each prop, all columns in the table MUST be filled. }
  | Prop Name | Type                                      | Required? | Default Value | Description                                                                                                |
  | :-------------- | :---------------------------------------- | :-------- | :------------ | :--------------------------------------------------------------------------------------------------------- |
  | `userId`        | `string`                                  | Yes       | N/A           | The ID of the user to display. MUST be a valid UUID.                                                     |
  | `avatarUrl`     | `string \| null`                          | No        | `null`        | URL for the user\'s avatar image. MUST be a valid HTTPS URL if provided.                                    |
  | `onEdit`        | `() => void`                              | No        | N/A           | Callback function when an edit action is triggered.                                                        |
  | `variant`       | `\'compact\' \| \'full\'`                     | No        | `\'full\'`        | Controls the display mode of the card.                                                                   |
  | `{anotherProp}` | `{Specific primitive, imported type, or inline interface/type definition}` | {Yes/No}  | {If any}    | {MUST clearly state the prop\'s purpose and any constraints, e.g., \'Must be a positive integer.\'}         |
- **Internal State (if any):**
  { Describe any significant internal state the component manages. Only list state that is *not* derived from props or global state. If state is complex, consider if it should be managed by a custom hook or global state solution instead. }
  | State Variable | Type      | Initial Value | Description                                                                    |
  | :-------------- | :-------- | :------------ | :----------------------------------------------------------------------------- |
  | `isLoading`     | `boolean` | `false`       | Tracks if data for the component is loading.                                   |
  | `{anotherState}`| `{type}`  | `{value}`     | {Description of state variable and its purpose.}                               |
- **Key UI Elements / Structure:**
  { Provide a pseudo-HTML or JSX-like structure representing the component\'s DOM. Include key conditional rendering logic if applicable. **This structure dictates the primary output for the AI agent.** }
  ```html
  <div> <!-- Main card container with specific class e.g., styles.cardFull or styles.cardCompact based on variant prop -->
    <img src="{avatarUrl || defaultAvatar}" alt="User Avatar" class="{styles.avatar}" />
    <h2>{userName}</h2>
    <p class="{variant === 'full' ? styles.emailFull : styles.emailCompact}">{userEmail}</p>
    {variant === 'full' && onEdit && <button onClick={onEdit} class="{styles.editButton}">Edit</button>}
  </div>
  ```
- **Events Handled / Emitted:**
  - **Handles:** {e.g., `onClick` on the edit button (triggers `onEdit` prop).}
  - **Emits:** {If the component emits custom events/callbacks not covered by props, describe them with their exact signature. e.g., `onFollow: (payload: { userId: string; followed: boolean }) => void`}
- **Actions Triggered (Side Effects):**
  - **State Management:** {e.g., "Dispatches `userSlice.actions.setUserName(newName)` from `src/store/slices/userSlice.ts`. Action payload MUST match the defined action creator." OR "Calls `updateUserProfileOptimistic(newData)` from a local `useReducer` hook."}
  - **API Calls:** {Specify which service/function from the "API Interaction Layer" is called. e.g., "Calls `userService.fetchUser(userId)` from `src/services/userService.ts` on mount. Request payload: `{ userId }`. Success response populates internal state `userData`. Error response dispatches `uiSlice.actions.showErrorToast({ message: 'Failed to load user details' })`.}
- **Styling Notes:**
  - {MUST reference specific Design System component names (e.g., "Uses `<Button variant='primary'>` from UI library") OR specify Tailwind CSS classes / CSS module class names to be applied (e.g., "Container uses `p-4 bg-white rounded-lg shadow-md`. Title uses `text-xl font-semibold`.") OR specify SCSS custom component classes to be applied (e.g., "Container uses `@apply p-4 bg-white rounded-lg shadow-md`. Title uses `@apply text-xl font-semibold`."). Any dynamic styling logic based on props or state MUST be described. If Tailwind CSS is used, list primary utility classes or `@apply` directives for custom component classes. AI Agent should prioritize direct utility class usage for simple cases and propose reusable component classes/React components for complex styling patterns.}
- **Accessibility Notes:**
  - {MUST list specific ARIA attributes and their values (e.g., `aria-label="User profile card"`, `role="article"`), required keyboard navigation behavior (e.g., "Tab navigates to avatar, name, email, then edit button. Edit button is focusable and activated by Enter/Space."), and any focus management requirements (e.g., "If this component opens a modal, focus MUST be trapped inside. On modal close, focus returns to the trigger element.").}

---

_Repeat the above template for each significant component._

---

## State Management In-Depth

{ This section expands on the State Management strategy. **Refer to the main Architecture Document for the definitive choice of state management solution.** }

- **Chosen Solution:** {e.g., Redux Toolkit, Zustand, Vuex, NgRx - As defined in main arch doc.}
- **Decision Guide for State Location:**
    - **Global State (e.g., Redux/Zustand):** Data shared across many unrelated components; data persisting across routes; complex state logic managed via reducers/thunks. **MUST be used for session data, user preferences, application-wide notifications.**
    - **React Context API:** State primarily passed down a specific component subtree (e.g., theme, form context). Simpler state, fewer updates compared to global state. **MUST be used for localized state not suitable for prop drilling but not needed globally.**
    - **Local Component State (`useState`, `useReducer`):** UI-specific state, not needed outside the component or its direct children (e.g., form input values, dropdown open/close status). **MUST be the default choice unless criteria for Context or Global State are met.**

### Store Structure / Slices

{ Describe the conventions for organizing the global state (e.g., "Each major feature requiring global state will have its own Redux slice located in `src/features/[featureName]/store.ts`"). }

- **Core Slice Example (e.g., `sessionSlice` in `src/store/slices/sessionSlice.ts`):**
  - **Purpose:** {Manages user session, authentication status, and basic user profile info accessible globally.}
  - **State Shape (Interface/Type):**
    ```typescript
    interface SessionState {
      currentUser: { id: string; name: string; email: string; roles: string[]; } | null;
      isAuthenticated: boolean;
      token: string | null;
      status: "idle" | "loading" | "succeeded" | "failed";
      error: string | null;
    }
    ```
  - **Key Reducers/Actions (within `createSlice`):** {Briefly list main synchronous actions, e.g., `setCurrentUser`, `clearSession`, `setAuthStatus`, `setAuthError`.}
  - **Async Thunks (if any):** {List key async thunks, e.g., `loginUserThunk`, `fetchUserProfileThunk`.}
  - **Selectors (memoized with `createSelector`):** {List key selectors, e.g., `selectCurrentUser`, `selectIsAuthenticated`.}
- **Feature Slice Template (e.g., `{featureName}Slice` in `src/features/{featureName}/store.ts`):**
  - **Purpose:** {To be filled out when a new feature requires its own state slice.}
  - **State Shape (Interface/Type):** {To be defined by the feature.}
  - **Key Reducers/Actions (within `createSlice`):** {To be defined by the feature.}
  - **Async Thunks (if any, defined using `createAsyncThunk`):** {To be defined by the feature.}
  - **Selectors (memoized with `createSelector`):** {To be defined by the feature.}
  - **Export:** {All actions and selectors MUST be exported.}

### Key Selectors

{ List important selectors for any core, upfront slices. For emergent feature slices, selectors will be defined with the slice. **ALL selectors deriving data or combining multiple state pieces MUST use `createSelector` from Reselect (or equivalent for other state libraries) for memoization.** }

- **`selectCurrentUser` (from `sessionSlice`):** {Returns the `currentUser` object.}
- **`selectIsAuthenticated` (from `sessionSlice`):** {Returns `isAuthenticated` boolean.}
- **`selectAuthToken` (from `sessionSlice`):** {Returns the `token` from `sessionSlice`.}

### Key Actions / Reducers / Thunks

{ Detail more complex actions for core, upfront slices, especially asynchronous thunks or sagas. Each thunk MUST clearly define its purpose, parameters, API calls made (referencing the API Interaction Layer), and how it updates the state on pending, fulfilled, and rejected states. }

- **Core Action/Thunk Example: `authenticateUser(credentials: AuthCredentials)` (in `sessionSlice.ts`):**
  - **Purpose:** {Handles user login by calling the auth API and updating the `sessionSlice`.}
  - **Parameters:** `credentials: { email: string; password: string }`
  - **Dispatch Flow (using Redux Toolkit `createAsyncThunk`):**
    1. On `pending`: Dispatches `sessionSlice.actions.setAuthStatus('loading')`.
    2. Calls `authService.login(credentials)` (from `src/services/authService.ts`).
    3. On `fulfilled` (success): Dispatches `sessionSlice.actions.setCurrentUser(response.data.user)`, `sessionSlice.actions.setToken(response.data.token)`, `sessionSlice.actions.setAuthStatus('succeeded')`.
    4. On `rejected` (error): Dispatches `sessionSlice.actions.setAuthError(error.message)`, `sessionSlice.actions.setAuthStatus('failed')`.
- **Feature Action/Thunk Template: `{featureActionName}` (in `{featureName}Slice.ts`):**
  - **Purpose:** {To be filled out for feature-specific async operations.}
  - **Parameters:** {Define specific parameters with types.}
  - **Dispatch Flow (using `createAsyncThunk`):** {To be defined by the feature, following similar patterns for pending, fulfilled, rejected states, including API calls and state updates.}

## API Interaction Layer

{ Describe how the frontend communicates with the backend APIs defined in the main Architecture Document. }

### Client/Service Structure

- **HTTP Client Setup:** {e.g., Axios instance in `src/services/apiClient.ts`. **MUST** include: Base URL (from environment variable `NEXT_PUBLIC_API_URL` or equivalent), default headers (e.g., `Content-Type: 'application/json'`), interceptors for automatic auth token injection (from state management, e.g., `sessionSlice.token`) and standardized error handling/normalization (see below).}
- **Service Definitions (Example):**
  - **`userService.ts` (in `src/services/userService.ts`):**
    - **Purpose:** {Handles all API interactions related to users.}
    - **Functions:** Each service function MUST have explicit parameter types, a return type (e.g., `Promise<User>`), JSDoc/TSDoc explaining purpose, params, return value, and any specific error handling. It MUST call the configured HTTP client (`apiClient`) with correct endpoint, method, and payload.
      - `fetchUser(userId: string): Promise<User>`
      - `updateUserProfile(userId: string, data: UserProfileUpdateDto): Promise<User>`
  - **`productService.ts` (in `src/services/productService.ts`):**
    - **Purpose:** {...}
    - **Functions:** {...}

### Error Handling & Retries (Frontend)

- **Global Error Handling:** {How are API errors caught globally? (e.g., Via Axios response interceptor in `apiClient.ts`). How are they presented/logged? (e.g., Dispatches `uiSlice.actions.showGlobalErrorBanner({ message: error.message })`, logs detailed error to console/monitoring service). Is there a global error state? (e.g., `uiSlice.error`).}
- **Specific Error Handling:** {Components MAY handle specific API errors locally for more contextual feedback (e.g., displaying an inline message on a form field: "Invalid email address"). This MUST be documented in the component's specification if it deviates from global handling.}
- **Retry Logic:** {Is client-side retry logic implemented (e.g., using `axios-retry` with `apiClient`)? If so, specify configuration: max retries (e.g., 3), retry conditions (e.g., network errors, 5xx server errors), retry delay (e.g., exponential backoff). **MUST apply only to idempotent requests (GET, PUT, DELETE).**}

## Routing Strategy

{ Detail how navigation and routing are handled in the frontend application. }

- **Routing Library:** {e.g., React Router, Next.js App Router, Vue Router, Angular Router. As per main Architecture Document.}

### Route Definitions

{ List the main routes of the application and the primary component/page rendered for each. }

| Path Pattern           | Component/Page (`src/app/...` or `src/pages/...`) | Protection                      | Notes                                                 |
| :--------------------- | :-------------------------------------------------- | :------------------------------ | :---------------------------------------------------- |
| `/`                    | `app/page.tsx` or `pages/HomePage.tsx`              | `Public`                        |                                                       |
| `/login`               | `app/login/page.tsx` or `pages/LoginPage.tsx`       | `Public` (redirect if auth)     | Redirects to `/dashboard` if already authenticated.   |
| `/dashboard`           | `app/dashboard/page.tsx` or `pages/DashboardPage.tsx` | `Authenticated`                 |                                                       |
| `/products`            | `app/products/page.tsx`                             | `Public`                        |                                                       |
| `/products/:productId` | `app/products/[productId]/page.tsx`                 | `Public`                        | Parameter: `productId` (string)                       |
| `/settings/profile`    | `app/settings/profile/page.tsx`                     | `Authenticated`, `Role:[USER]`  | Example of role-based protection.                   |
| `{anotherRoute}`       | `{ComponentPath}`                                   | `{Public/Authenticated/Role:[ROLE_NAME]}` | {Notes, parameter names and types}                    |

### Route Guards / Protection

- **Authentication Guard:** {Describe how routes are protected based on authentication status. **Specify the exact HOC, hook, layout, or middleware mechanism and its location** (e.g., `src/guards/AuthGuard.tsx`, or Next.js middleware in `middleware.ts`). Logic MUST use authentication state from the `sessionSlice` (or equivalent). Unauthenticated users attempting to access protected routes MUST be redirected to `/login` (or specified login path).}
- **Authorization Guard (if applicable):** {Describe how routes might be protected based on user roles or permissions. **Specify the exact mechanism**, similar to Auth Guard. Unauthorized users (authenticated but lacking permissions) MUST be shown a "Forbidden" page or redirected to a safe page.}

## Build, Bundling, and Deployment

{ Details specific to the frontend build and deployment process, complementing the "Infrastructure and Deployment Overview" in the main architecture document. }

### Build Process & Scripts

- **Key Build Scripts (from `package.json`):** {e.g., `"build": "next build"`. What do they do? Point to `package.json` scripts. `"dev": "next dev"`, `"start": "next start"`.}. **AI Agent MUST NOT generate code that hardcodes environment-specific values. All such values MUST be accessed via the defined environment configuration mechanism.** Specify the exact files and access method.
- **Environment Configuration Management:** {How are `process.env.NEXT_PUBLIC_API_URL` (or equivalent like `import.meta.env.VITE_API_URL`) managed for different environments (dev, staging, prod)? (e.g., `.env`, `.env.development`, `.env.production` files for Next.js/Vite; build-time injection via CI variables). Specify the exact files and access method.}

### Key Bundling Optimizations

- **Code Splitting:** {How is it implemented/ensured? (e.g., "Next.js/Vite handles route-based code splitting automatically. For component-level code splitting, dynamic imports `React.lazy(() => import('./MyComponent'))` or `import('./heavy-module')` MUST be used for non-critical large components/libraries.")}
- **Tree Shaking:** {How is it implemented/ensured? (e.g., "Ensured by modern build tools like Webpack/Rollup (used by Next.js/Vite) when using ES Modules. Avoid side-effectful imports in shared libraries.")}
- **Lazy Loading (Components, Images, etc.):** {Strategy for lazy loading. (e.g., "Components: `React.lazy` with `Suspense`. Images: Use framework-specific Image component like `next/image` which handles lazy loading by default, or `loading='lazy'` attribute for standard `<img>` tags.")}
- **Minification & Compression:** {Handled by build tools (e.g., Webpack/Terser, Vite/esbuild)? Specify if any specific configuration is needed. Compression (e.g., Gzip, Brotli) is typically handled by the hosting platform/CDN.}

### Deployment to CDN/Hosting

- **Target Platform:** {e.g., Vercel, Netlify, AWS S3/CloudFront, Azure Static Web Apps. As per main Architecture Document.}
- **Deployment Trigger:** {e.g., Git push to `main` branch via GitHub Actions (referencing main CI/CD pipeline).}
- **Asset Caching Strategy:** {How are static assets cached? (e.g., "Immutable assets (JS/CSS bundles with content hashes) have `Cache-Control: public, max-age=31536000, immutable`. HTML files have `Cache-Control: no-cache` or short max-age (e.g., `public, max-age=0, must-revalidate`) to ensure users get fresh entry points. Configured via {hosting platform settings / `next.config.js` headers / CDN rules}.}

## Frontend Testing Strategy

{ This section elaborates on the "Testing Strategy" from the main architecture document, focusing on frontend-specific aspects. **Refer to the main Architecture Document for definitive choices of testing tools.** }

- **Link to Main Overall Testing Strategy:** {Reference the main `docs/architecture.md#overall-testing-strategy` or equivalent.}

### Component Testing

- **Scope:** {Testing individual UI components in isolation (similar to unit tests for components).}
- **Tools:** {e.g., React Testing Library with Jest, Vitest, Vue Test Utils, Angular Testing Utilities. As per main Arch Doc.}
- **Focus:** {Rendering with various props, user interactions (clicks, input changes using `fireEvent` or `userEvent`), event emission, basic internal state changes. **Snapshot testing MUST be used sparingly and with clear justification (e.g., for very stable, purely presentational components with complex DOM structure); prefer explicit assertions.**}
- **Location:** {e.g., `*.test.tsx` or `*.spec.tsx` co-located alongside components, or in a `__tests__` subdirectory.}

### Feature/Flow Testing (UI Integration)

- **Scope:** {Testing how multiple components interact to fulfill a small user flow or feature within a page, potentially mocking API calls or global state management. e.g., testing a complete form submission within a feature, including validation and interaction with a mocked service layer.}
- **Tools:** {Same as component testing (e.g., React Testing Library with Jest/Vitest), but with more complex setups involving mock providers for routing, state, API calls.}
- **Focus:** {Data flow between components, conditional rendering based on interactions, navigation within a feature, integration with mocked services/state.}

### End-to-End UI Testing Tools & Scope

- **Tools:** {Reiterate from main Testing Strategy, e.g., Playwright, Cypress, Selenium.}
- **Scope (Frontend Focus):** {Define 3-5 key user journeys that MUST be covered by E2E UI tests from a UI perspective, e.g., "User registration and login flow", "Adding an item to cart and proceeding to the checkout page summary", "Submitting a complex multi-step form and verifying success UI state and data persistence (via API mocks or a test backend)."}
- **Test Data Management for UI:** {How is consistent test data seeded or mocked for UI E2E tests? (e.g., API mocking layer like MSW, backend seeding scripts, dedicated test accounts).}

## Accessibility (AX) Implementation Details

{ Based on the AX requirements in the UI/UX Specification, detail how these will be technically implemented with comprehensive validation frameworks and evidence requirements. }

### Accessibility Standards & Compliance

- **Target Compliance Level:** WCAG 2.1 Level AA (minimum) with Level AAA for critical user paths
- **Legal Requirements:** {Specify any ADA, Section 508, EN 301 549, or other regional requirements}

### Implementation Requirements

- **Semantic HTML:**
  - Mandate: **AI Agent MUST prioritize semantic elements (e.g., `<nav>`, `<button>`, `<article>`) over generic `<div>`/`<span>` with ARIA roles where a native element exists.**
  - Evidence Requirements:
    - [ ] HTML validation passes with zero errors
    - [ ] Semantic structure audit in every component review
    - [ ] Documented rationale for any non-semantic element usage

- **ARIA Implementation:**
  - Required Patterns: {e.g., "Custom select dropdown MUST follow ARIA Combobox pattern. Custom Tabs MUST follow ARIA Tabbed Interface pattern."}
  - Evidence Requirements:
    - [ ] ARIA pattern compliance documentation per component
    - [ ] Link to ARIA APG reference for each pattern used
    - [ ] Automated ARIA validation in component tests

- **Keyboard Navigation:**
  - Requirements: All interactive elements MUST be keyboard accessible with logical focus order
  - Evidence Requirements:
    - [ ] Keyboard navigation test matrix for all components
    - [ ] Focus order documentation and testing
    - [ ] Tab trap implementation for modals/overlays

- **Focus Management:**
  - Requirements: {e.g., "Modals MUST trap focus. Route changes MUST manage focus appropriately."}
  - Evidence Requirements:
    - [ ] Focus management strategy documented
    - [ ] Automated focus tests for dynamic content
    - [ ] Manual testing checklist completed

### Accessibility Validation Framework

- **Automated Testing:**
  | Tool | Integration Point | Failure Threshold | Evidence Output |
  | :--- | :--- | :--- | :--- |
  | jest-axe | Component unit tests | Zero violations | Test reports |
  | Lighthouse | CI/CD pipeline | Score > 90 | HTML reports |
  | Pa11y | E2E test suite | WCAG AA violations = 0 | JSON reports |
  | axe-playwright | Integration tests | Critical issues = 0 | CI artifacts |

- **Manual Testing Requirements:**
  | Test Type | Frequency | Tools | Evidence Required |
  | :--- | :--- | :--- | :--- |
  | Screen Reader | Every sprint | NVDA, JAWS, VoiceOver | Video recordings |
  | Keyboard Only | Every component | Native keyboard | Navigation matrix |
  | Color Contrast | Design phase | Contrast analyzers | Design approval |
  | Zoom Testing | Quarterly | Browser zoom 200% | Screenshots |

### Component-Level Accessibility Requirements

- **For Each Component:**
  - [ ] Accessibility specification defined
  - [ ] ARIA roles and properties documented
  - [ ] Keyboard interaction patterns specified
  - [ ] Screen reader announcements defined
  - [ ] Error handling accessible
  - [ ] Loading states announced
  - [ ] Focus indicators visible

### Accessibility Evidence Collection

- **Documentation Requirements:**
  | Evidence Type | Storage Location | Review Frequency |
  | :--- | :--- | :--- |
  | Automated test results | `.accessibility/automated/` | Every PR |
  | Manual test recordings | `.accessibility/manual/` | Sprint review |
  | VPAT documentation | `.accessibility/vpat/` | Quarterly |
  | User testing feedback | `.accessibility/user-feedback/` | As collected |

- **Accessibility Checklist (Per Feature):**
  - [ ] Automated tests passing (jest-axe, Pa11y)
  - [ ] Manual keyboard navigation verified
  - [ ] Screen reader testing completed (3 major readers)
  - [ ] Color contrast validated (4.5:1 minimum)
  - [ ] Focus indicators present and visible
  - [ ] Error messages associated with form controls
  - [ ] Loading and dynamic content announced
  - [ ] Alternative text for all informative images
  - [ ] Captions/transcripts for media content
  - [ ] Page structure uses proper heading hierarchy

## Performance Considerations

{ Highlight frontend-specific performance optimization strategies with measurable benchmarks and evidence requirements. }

### Performance Benchmarks & Evidence Requirements

- **Core Web Vitals Targets:**
  | Metric | Target | Evidence Required | Measurement Tool |
  | :--- | :--- | :--- | :--- |
  | Largest Contentful Paint (LCP) | < 2.5s | Lighthouse CI reports for each route | Lighthouse CI |
  | First Input Delay (FID) | < 100ms | Real User Monitoring (RUM) data | Web Vitals API |
  | Cumulative Layout Shift (CLS) | < 0.1 | Visual stability recordings | Lighthouse CI |
  | Time to Interactive (TTI) | < 3.5s | Performance trace analysis | Chrome DevTools |
  | Total Blocking Time (TBT) | < 300ms | Main thread analysis | Lighthouse CI |

- **Bundle Size Constraints:**
  | Bundle Type | Max Size (gzipped) | Evidence Required | Enforcement |
  | :--- | :--- | :--- | :--- |
  | Initial JS Bundle | 150KB | Webpack bundle analyzer report | CI build failure if exceeded |
  | Initial CSS Bundle | 50KB | CSS analysis report | CI warning if exceeded |
  | Per-Route Bundle | 100KB | Route-specific analysis | Manual review required |
  | Total App Size | 500KB | Complete bundle report | Quarterly review |

### Performance Optimization Strategies

- **Image Optimization:**
  - Implementation Mandate: {e.g., "All images MUST use `<Image>` component from Next.js (or equivalent framework-specific optimizer). SVGs for icons. WebP format preferred where supported."}
  - Evidence Requirements:
    - [ ] All images have defined width/height attributes (CLS prevention)
    - [ ] WebP variants provided for all raster images
    - [ ] Image loading strategy documented per component
    - [ ] Lighthouse image optimization score > 90

- **Code Splitting & Lazy Loading:**
  - Implementation Mandate: {e.g., "Next.js handles route-based code splitting automatically. Dynamic imports `import()` MUST be used for component-level lazy loading."}
  - Evidence Requirements:
    - [ ] Bundle analyzer shows proper code splitting
    - [ ] Coverage report shows < 60% initial code execution
    - [ ] Lazy loading boundaries documented in component specs

- **Render Performance:**
  - Implementation Mandate: {e.g., "`React.memo` MUST be used for components that render frequently with same props. Selectors for global state MUST be memoized (e.g., with Reselect)."}
  - Evidence Requirements:
    - [ ] React DevTools Profiler traces for critical paths
    - [ ] Documented re-render optimization strategies
    - [ ] Performance regression tests for key components

- **Runtime Performance:**
  - Implementation Mandate: {e.g., "Use utility functions for debouncing/throttling. Define specific wait times."}
  - Evidence Requirements:
    - [ ] Interaction performance traces
    - [ ] Main thread blocking analysis
    - [ ] User interaction response times < 50ms

### Performance Monitoring & Tracking

- **Continuous Monitoring:**
  - Real User Monitoring (RUM) integration required
  - Synthetic monitoring for key user journeys
  - Performance budgets enforced in CI/CD pipeline
  - Weekly performance regression reports

- **Evidence Collection:**
  | Performance Check | Frequency | Storage Location | Review Process |
  | :--- | :--- | :--- | :--- |
  | Lighthouse CI | Every PR | `.performance/lighthouse/` | Automated PR comment |
  | Bundle Analysis | Every build | `.performance/bundles/` | Manual review if size increased |
  | Runtime Traces | Weekly | `.performance/traces/` | Sprint retrospective |
  | RUM Dashboard | Continuous | Monitoring platform | Weekly team review |

## Internationalization (i18n) and Localization (l10n) Strategy

{This section defines the strategy for supporting multiple languages and regional differences if applicable. If not applicable, state "Internationalization is not a requirement for this project at this time."}

- **Requirement Level:** {e.g., Not Required, Required for specific languages [list them], Fully internationalized for future expansion.}
- **Chosen i18n Library/Framework:** {e.g., `react-i18next`, `vue-i18n`, `ngx-translate`, framework-native solution like Next.js i18n routing. Specify the exact library/mechanism.}
- **Translation File Structure & Format:** {e.g., JSON files per language per feature (`src/features/{featureName}/locales/{lang}.json`), or global files (`public/locales/{lang}.json`). Define the exact path and format (e.g., flat JSON, nested JSON).}
- **Translation Key Naming Convention:** {e.g., `featureName.componentName.elementText`, `common.submitButton`. MUST be a clear, consistent, and documented pattern.}
- **Process for Adding New Translatable Strings:** {e.g., "AI Agent MUST add new keys to the default language file (e.g., `en.json`) and use the i18n library's functions/components (e.g., `<Trans>` component, `t()` function) to render text. Keys MUST NOT be constructed dynamically at runtime in a way that prevents static analysis."}
- **Handling Pluralization:** {Specify method/syntax, e.g., using ICU message format via the chosen library (e.g., `t('key', { count: N })`).}
- **Date, Time, and Number Formatting:** {Specify if the i18n library handles this, or if another library (e.g., `date-fns-tz` with locale support, `Intl` API directly) and specific formats/styles should be used for each locale.}
- **Default Language:** {e.g., `en-US`}
- **Language Switching Mechanism (if applicable):** {How is the language changed by the user and persisted? e.g., "Via a language selector component that updates a global state/cookie and potentially alters the URL route."}

## Feature Flag Management

{This section outlines how conditionally enabled features are managed. If not applicable, state "Feature flags are not a primary architectural concern for this project at this time."}

- **Requirement Level:** {e.g., Not Required, Used for specific rollouts, Core part of development workflow.}
- **Chosen Feature Flag System/Library:** {e.g., LaunchDarkly, Unleash, Flagsmith, custom solution using environment variables or a configuration service. Specify the exact tool/method.}
- **Accessing Flags in Code:** {e.g., "Via a custom hook `useFeatureFlag('flag-name'): boolean` or a service `featureFlagService.isOn('flag-name')`. Specify the exact interface, location, and initialization of the service/provider."}
- **Flag Naming Convention:** {e.g., `[SCOPE]_[FEATURE_NAME]_[TARGET_GROUP_OR_TYPE]`, e.g., `CHECKOUT_NEW_PAYMENT_GATEWAY_ROLLOUT`, `USER_PROFILE_BETA_AVATAR_UPLOAD`. MUST be documented and consistently applied.}
- **Code Structure for Flagged Features:** {e.g., "Use conditional rendering (`{isFeatureEnabled && <NewComponent />}`). For larger features, conditionally import components (`React.lazy` with flag check) or routes. Avoid complex branching logic deep within shared components; prefer to flag at higher levels."}
- **Strategy for Code Cleanup (Post-Flag Retirement):** {e.g., "Once a flag is fully rolled out (100% users) and deemed permanent, or fully removed, all conditional logic, old code paths, and the flag itself MUST be removed from the codebase within {N, e.g., 2} sprints. This is a mandatory tech debt item."}
- **Testing Flagged Features:** {How are different flag variations tested? e.g., "QA team uses a debug panel to toggle flags. Automated E2E tests run with specific flag configurations."}

## Frontend Security Considerations

{This section highlights mandatory frontend-specific security practices, complementing the main Architecture Document. AI Agent MUST adhere to these guidelines.}

- **Cross-Site Scripting (XSS) Prevention:**
  - Framework Reliance: {e.g., "React's JSX auto-escaping MUST be relied upon for rendering dynamic content. Vue's `v-html` MUST be avoided unless content is explicitly sanitized."}
  - Explicit Sanitization: {If direct DOM manipulation is unavoidable (strongly discouraged), use {specific sanitization library/function like DOMPurify}. Specify its configuration.}
  - Content Security Policy (CSP): {Is a CSP implemented? How? e.g., "CSP is enforced via HTTP headers set by the backend/CDN as defined in the main Architecture doc. Frontend MAY need to ensure nonce usage for inline scripts if `unsafe-inline` is not allowed." Link to CSP definition if available.}
- **Cross-Site Request Forgery (CSRF) Protection (if applicable for session-based auth):**
  - Mechanism: {e.g., "Backend uses synchronizer token pattern. Frontend ensures tokens are included in state-changing requests if not handled automatically by HTTP client or forms." Refer to main Architecture Document for backend details.}
- **Secure Token Storage & Handling (for client-side tokens like JWTs):**
  - Storage Mechanism: {**MUST specify exact mechanism**: e.g., In-memory via state management (e.g., Redux/Zustand store, cleared on tab close), `HttpOnly` cookies (if backend sets them and frontend doesn't need to read them), `sessionStorage`. **`localStorage` is STRONGLY DISCOURAGED for token storage.**}
  - Token Refresh: {Describe client-side involvement, e.g., "Interceptor in `apiClient.ts` handles 401 errors to trigger token refresh endpoint."}
- **Third-Party Script Security:**
  - Policy: {e.g., "All third-party scripts (analytics, ads, widgets) MUST be vetted for necessity and security. Load scripts asynchronously (`async/defer`)."}
  - Subresource Integrity (SRI): {e.g., "SRI hashes MUST be used for all external scripts and stylesheets loaded from CDNs where the resource is stable."}
- **Client-Side Data Validation:**
  - Purpose: {e.g., "Client-side validation is for UX improvement (immediate feedback) ONLY. **All critical data validation MUST occur server-side** (as defined in the main Architecture Document)."}
  - Implementation: {e.g., "Use {form_library_name like Formik/React Hook Form} for form validation. Rules should mirror server-side validation where appropriate."}
- **Preventing Clickjacking:**
  - Mechanism: {e.g., "Primary defense is `X-Frame-Options` or `frame-ancestors` CSP directive, set by backend/CDN. Frontend code should not rely on frame-busting scripts."}
- **API Key Exposure (for client-side consumed services):**
  - Restriction: {e.g., "API keys for services like Google Maps (client-side JS SDK) MUST be restricted (e.g., HTTP referrer, IP address, API restrictions) via the service provider's console."}
  - Backend Proxy: {e.g., "For keys requiring more secrecy or involving sensitive operations, a backend proxy endpoint MUST be created; frontend calls the proxy, not the third-party service directly."}
- **Secure Communication (HTTPS):**
  - Mandate: {e.g., "All communication with backend APIs MUST use HTTPS. Mixed content (HTTP assets on HTTPS page) is forbidden."}
- **Dependency Vulnerabilities:**
  - Process: {e.g., "Run `npm audit --audit-level=high` (or equivalent) in CI. High/critical vulnerabilities MUST be addressed before deployment. Monitor Dependabot/Snyk alerts."}

## User Experience Validation Requirements

{ Define comprehensive user experience validation with measurable metrics and evidence requirements. }

### UX Metrics & Targets

- **User Satisfaction Metrics:**
  | Metric | Target | Measurement Method | Frequency |
  | :--- | :--- | :--- | :--- |
  | Task Success Rate | > 95% | User testing sessions | Per feature |
  | Time on Task | < baseline + 20% | Session recordings | Sprint review |
  | Error Rate | < 5% | Analytics tracking | Continuous |
  | User Satisfaction Score | > 4.5/5 | In-app surveys | Monthly |
  | Net Promoter Score (NPS) | > 50 | Email surveys | Quarterly |

- **Usability Testing Requirements:**
  | Test Type | Participants | Evidence Required | Frequency |
  | :--- | :--- | :--- | :--- |
  | Moderated Testing | 5-8 users | Video recordings, findings report | Major features |
  | Unmoderated Testing | 15-20 users | Task completion data, heatmaps | Minor features |
  | A/B Testing | Statistical significance | Analytics reports, decision log | As needed |
  | Card Sorting | 10-15 users | Information architecture validation | IA changes |

### User Flow Validation

- **Critical User Journeys:**
  - [ ] User journey maps created and validated
  - [ ] Task flow diagrams with success criteria
  - [ ] Error recovery paths documented
  - [ ] Drop-off points identified and addressed
  - [ ] Alternative paths for different user types

- **Interaction Design Evidence:**
  | Element | Validation Required | Evidence Type |
  | :--- | :--- | :--- |
  | Micro-interactions | User feedback positive | Session recordings |
  | Loading states | Perceived performance < 3s | Performance metrics |
  | Error messages | Clear and actionable | Usability test results |
  | Empty states | Helpful and engaging | Screenshot approval |
  | Success feedback | Noticeable but not intrusive | User feedback |

### Analytics & Monitoring

- **User Behavior Tracking:**
  - [ ] Analytics implementation plan
  - [ ] Event tracking taxonomy defined
  - [ ] Conversion funnel instrumentation
  - [ ] Rage click detection enabled
  - [ ] Session replay capability

- **UX Performance Indicators:**
  | KPI | Target | Alert Threshold | Dashboard |
  | :--- | :--- | :--- | :--- |
  | Bounce Rate | < 40% | > 50% | Real-time |
  | Session Duration | > 2 min | < 1 min | Daily |
  | Pages per Session | > 3 | < 2 | Daily |
  | Form Completion Rate | > 80% | < 60% | Real-time |
  | Search Success Rate | > 90% | < 70% | Weekly |

## Responsive Design Evidence & Requirements

{ Define comprehensive responsive design validation with device coverage and evidence requirements. }

### Device & Viewport Coverage

- **Required Breakpoints:**
  | Breakpoint | Width | Device Category | Testing Required |
  | :--- | :--- | :--- | :--- |
  | Mobile Small | 320px | Small phones | Physical device |
  | Mobile | 375px | Standard phones | Emulator + device |
  | Mobile Large | 414px | Large phones | Emulator + device |
  | Tablet | 768px | Tablets portrait | Physical device |
  | Tablet Landscape | 1024px | Tablets landscape | Physical device |
  | Desktop | 1280px | Small laptops | Required |
  | Desktop Large | 1440px | Standard monitors | Required |
  | Desktop XL | 1920px+ | Large monitors | Required |

### Responsive Testing Requirements

- **Cross-Device Testing Matrix:**
  | Test Type | Coverage | Evidence | Tools |
  | :--- | :--- | :--- | :--- |
  | Visual Testing | All breakpoints | Screenshots | BrowserStack |
  | Interaction Testing | Touch + mouse | Video recordings | Real devices |
  | Performance Testing | 3G/4G/WiFi | Performance reports | WebPageTest |
  | Orientation Testing | Portrait + landscape | Test reports | Device lab |

- **Responsive Design Checklist:**
  - [ ] Fluid typography scaling implemented
  - [ ] Images responsive with proper srcset
  - [ ] Touch targets minimum 44x44px
  - [ ] Horizontal scrolling prevented
  - [ ] Content reflow without data loss
  - [ ] Navigation adapts to screen size
  - [ ] Forms usable on all devices
  - [ ] Tables have responsive solution

### Adaptive Features

- **Progressive Enhancement by Device:**
  | Feature | Mobile | Tablet | Desktop | Evidence |
  | :--- | :--- | :--- | :--- | :--- |
  | Navigation | Hamburger menu | Hybrid | Full menu | Screenshots |
  | Images | Compressed | Standard | High-res | Performance data |
  | Animations | Reduced | Standard | Full | Performance profiles |
  | Interactions | Touch-first | Mixed | Hover states | Interaction maps |

- **Performance Budget by Device Type:**
  | Device | First Paint | Interactive | Total Size | Evidence |
  | :--- | :--- | :--- | :--- | :--- |
  | Mobile (3G) | < 3s | < 5s | < 300KB | WebPageTest |
  | Mobile (4G) | < 1.5s | < 3s | < 500KB | Lighthouse |
  | Desktop | < 1s | < 2s | < 1MB | RUM data |

### Evidence Collection

- **Responsive Design Artifacts:**
  | Artifact Type | Format | Location | Review Process |
  | :--- | :--- | :--- | :--- |
  | Device Screenshots | PNG/WebP | `.responsive/screenshots/` | Design review |
  | Interaction Videos | MP4 | `.responsive/videos/` | UX review |
  | Performance Reports | JSON/HTML | `.responsive/performance/` | Tech review |
  | Test Results | JSON | `.responsive/tests/` | QA sign-off |

## Browser Support and Progressive Enhancement

{This section defines the target browsers and how the application should behave in less capable or non-standard environments.}

- **Target Browsers:** {e.g., "Latest 2 stable versions of Chrome, Firefox, Safari, Edge. Specific versions can be listed if required by project constraints. Internet Explorer (any version) is NOT supported." MUST be explicit.}
- **Polyfill Strategy:**
  - Mechanism: {e.g., "Use `core-js@3` imported at the application entry point. Babel `preset-env` is configured with the above browser targets to include necessary polyfills."}
  - Specific Polyfills (if any beyond `core-js`): {List any other polyfills required for specific features, e.g., `smoothscroll-polyfill`.}
- **JavaScript Requirement & Progressive Enhancement:**
  - Baseline: {e.g., "Core application functionality REQUIRES JavaScript enabled in the browser." OR "Key content (e.g., articles, product information) and primary navigation MUST be accessible and readable without JavaScript. Interactive features and enhancements are layered on top with JavaScript (Progressive Enhancement approach)." Specify the chosen approach.}
  - No-JS Experience (if Progressive Enhancement): {Describe what works without JS. e.g., "Users can view pages and navigate. Forms may not submit or will use standard HTML submission."}
- **CSS Compatibility & Fallbacks:**
  - Tooling: {e.g., "Use Autoprefixer (via PostCSS) configured with the target browser list to add vendor prefixes."}
  - Feature Usage: {e.g., "Avoid CSS features not supported by >90% of target browsers unless a graceful degradation or fallback is explicitly defined and tested (e.g., using `@supports` queries)."}
- **Accessibility Fallbacks:** {Consider how features behave if certain ARIA versions or advanced accessibility features are not supported by older assistive technologies within the support matrix.}

## Change Log

| Change | Date | Version | Description | Author |
| ------ | ---- | ------- | ----------- | ------ |
