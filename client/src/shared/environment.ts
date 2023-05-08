import { z } from 'zod'

export const envVariables = z.object({
  NEXT_PUBLIC_API_URL: z.string(),
})

envVariables.parse(process.env)
