import { envVariables } from "@shared/environment";
import { PWB_LABELS } from "@shared/constants";
declare global {
  namespace NodeJS {
    interface ProcessEnv extends z.infer<typeof envVariables> {}
  }
}

export type PWBLabel = (typeof PWB_LABELS)[number];
