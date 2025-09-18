# CLAUDE.md - Next.js Expert Configuration

## Overview
This guide configures Claude Code to be fluent and expert in Next.js development, following the official Next.js 15.5.3 App Router project structure and conventions.

## Next.js Project Structure Expertise

### Top-Level Organization
- **`app/`** - Primary App Router directory for routing and layouts
- **`pages/`** - Legacy Pages Router (use App Router for new projects)
- **`public/`** - Static assets served from root
- **`src/`** - Optional source folder to separate app code from config

### Configuration Files
- **`next.config.js`** - Main Next.js configuration
- **`package.json`** - Dependencies and scripts
- **`instrumentation.ts`** - OpenTelemetry monitoring
- **`middleware.ts`** - Request middleware
- **Environment files** - `.env`, `.env.local`, `.env.production`, `.env.development`
- **TypeScript/ESLint** - `tsconfig.json`, `.eslintrc.json`

### App Router File Conventions

#### Core Routing Files
```
app/
├── layout.tsx          # Root layout (required)
├── page.tsx           # Home page route
├── loading.tsx        # Loading UI
├── error.tsx          # Error boundaries
├── not-found.tsx      # 404 pages
└── global-error.tsx   # Global error handler
```

#### Special Files
- **`layout.js/tsx`** - Shared UI that wraps child segments
- **`page.js/tsx`** - Unique UI for a route (makes route publicly accessible)
- **`loading.js/tsx`** - Loading UI with React Suspense
- **`error.js/tsx`** - Error UI with React Error Boundaries
- **`not-found.js/tsx`** - UI for 404 errors
- **`route.js/ts`** - API endpoints
- **`template.js/tsx`** - Re-rendered layout template
- **`default.js/tsx`** - Parallel route fallback

### Dynamic Routes
- **`[slug]/`** - Single dynamic segment
- **`[...slug]/`** - Catch-all segments
- **`[[...slug]]/`** - Optional catch-all segments

### Advanced Routing Patterns
- **`(group)/`** - Route groups (excluded from URL)
- **`_folder/`** - Private folders (not routable)
- **`@slot/`** - Parallel routes (named slots)
- **`(.)folder/`** - Intercepting routes

### Metadata Files
- **`favicon.ico`** - Favicon
- **`icon.png/svg`** - App icons
- **`apple-icon.png`** - Apple touch icons
- **`opengraph-image.png`** - Open Graph images
- **`twitter-image.png`** - Twitter card images
- **`sitemap.xml`** - SEO sitemap
- **`robots.txt`** - Search crawler rules

## Development Best Practices

### Component Organization
1. **Hierarchy**: `layout` → `template` → `error` → `loading` → `not-found` → `page`
2. **Colocation**: Components can be safely placed alongside routes
3. **Private folders**: Use `_components/`, `_lib/`, `_utils/` for non-routable code

### Project Organization Strategies

#### Strategy 1: External Organization
```
project/
├── app/                 # Routes only
├── components/          # Shared components
├── lib/                # Utilities
├── styles/             # Global styles
└── types/              # TypeScript types
```

#### Strategy 2: App-Centric Organization
```
app/
├── _components/        # Shared components
├── _lib/              # Utilities
├── _styles/           # Styles
├── (auth)/            # Route group
│   ├── login/
│   └── register/
└── dashboard/
    ├── _components/   # Dashboard-specific components
    └── page.tsx
```

#### Strategy 3: Feature-Based Organization
```
app/
├── _components/       # Global components
├── _lib/             # Global utilities
├── (marketing)/
│   ├── _components/  # Marketing components
│   ├── about/
│   └── pricing/
└── (app)/
    ├── _components/  # App components
    ├── dashboard/
    └── settings/
```

### Route Groups Usage
- **Organization**: `(marketing)`, `(app)`, `(admin)`
- **Multiple layouts**: Different `layout.tsx` in each group
- **Conditional layouts**: Apply layouts to specific route subsets

## File Naming Conventions

### Required Naming
- Use exact names: `page.tsx`, `layout.tsx`, `loading.tsx`
- API routes: `route.ts` (not `api.ts` or `handler.ts`)
- Metadata: `icon.png`, `opengraph-image.jpg`

### Custom File Naming
- Components: `PascalCase` (e.g., `UserProfile.tsx`)
- Utilities: `camelCase` (e.g., `formatDate.ts`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `API_ENDPOINTS.ts`)

## TypeScript Integration

### Recommended Structure
```typescript
// app/layout.tsx
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'App Name',
  description: 'App description'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

### Page Props
```typescript
// app/blog/[slug]/page.tsx
interface PageProps {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export default async function Page({ params, searchParams }: PageProps) {
  const { slug } = await params
  // Component logic
}
```

## Performance Optimizations

### Server vs Client Components
- **Default**: Server Components (better performance)
- **Client**: Use `"use client"` directive when needed for interactivity
- **Server Actions**: Use `"use server"` for form handling

### Image Optimization
```typescript
import Image from 'next/image'

// Optimized images
<Image
  src="/hero.jpg"
  alt="Hero image"
  width={800}
  height={600}
  priority // For above-the-fold images
/>
```

### Font Optimization
```typescript
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

## Data Fetching Patterns

### Server Components (Recommended)
```typescript
// Direct data fetching in Server Components
export default async function Page() {
  const data = await fetch('https://api.example.com/data')
  const result = await data.json()
  
  return <div>{result.title}</div>
}
```

### Client Components
```typescript
"use client"
import { useState, useEffect } from 'react'

export default function ClientComponent() {
  const [data, setData] = useState(null)
  
  useEffect(() => {
    fetch('/api/data').then(res => res.json()).then(setData)
  }, [])
  
  return <div>{data?.title}</div>
}
```

## Common Commands & Setup

### Project Creation
```bash
npx create-next-app@latest my-app --typescript --tailwind --eslint --app
```

### Development Commands
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
npm run lint         # Run ESLint
```

### Key Dependencies
```json
{
  "dependencies": {
    "next": "^15.5.3",
    "react": "^18",
    "react-dom": "^18"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "^15.5.3",
    "typescript": "^5"
  }
}
```

## Troubleshooting Guidelines

### Common Issues
1. **Hydration errors**: Check server/client component boundaries
2. **Import errors**: Verify file paths and extensions
3. **Build failures**: Check TypeScript errors and unused dependencies
4. **Route conflicts**: Ensure proper file naming conventions

### Debugging
- Use Next.js built-in error overlay
- Check browser dev tools for hydration mismatches
- Verify API routes with network tab
- Use React Developer Tools for component debugging

## Expert Recommendations

1. **Always use App Router** for new projects (not Pages Router)
2. **Start with Server Components** and add client components only when needed
3. **Follow the official file conventions** exactly as documented
4. **Use TypeScript** for better developer experience and catch errors early
5. **Implement proper error boundaries** and loading states
6. **Optimize images and fonts** using Next.js built-in components
7. **Structure projects consistently** using one of the recommended organization patterns
8. **Use route groups** for complex applications with multiple sections
9. **Implement proper SEO** with metadata files and structured data
10. **Test thoroughly** with both development and production builds

This configuration ensures Claude Code provides expert-level Next.js guidance following the latest official conventions and best practices.