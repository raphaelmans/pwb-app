import { ResultImageRoutes, evaluateMutation } from "@shared/services";
import useSWRMutation from "swr/mutation";

export const useEvaluate = () => {
  const { trigger: evaluateImg, isMutating } = useSWRMutation(
    ResultImageRoutes.evaluatePWB,
    evaluateMutation,
    {
      revalidate: true,
    }
  );

  return {
    evaluateImg,
    isMutating,
  };
};
