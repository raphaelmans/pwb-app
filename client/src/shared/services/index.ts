import baseFetcher from "@shared/api";
import { PWBLabel } from "@types";
import { AxiosResponse } from "axios";
import { MutationFetcher } from "swr/mutation";

type ResultImage = {
  datauri: string;
};

const ResultImageRoutes = {
  saveImage: "/save_image",
  evaluatePWB: "/evaluate_pwb",
};

const ResultImageService = {
  saveImage: (base64Img: string) => {
    return baseFetcher.post<ResultImage, any>(ResultImageRoutes.saveImage, {
      datauri: base64Img,
    });
  },
  evaluate_pwb: (base64Img: string) => {
    return baseFetcher.post<ResultImage, any>(ResultImageRoutes.evaluatePWB, {
      datauri: base64Img,
    });
  },
};

const saveImageMutation: MutationFetcher<
  AxiosResponse<any>,
  ResultImage,
  string
> = (_, { arg }) => {
  return ResultImageService.saveImage(arg.datauri);
};

const evaluateMutation: MutationFetcher<
  AxiosResponse<EvaluationResult>,
  ResultImage,
  string
> = (_, { arg }) => {
  return ResultImageService.evaluate_pwb(arg.datauri);
};
export type EvaluationResult = {
  result: {
    label: PWBLabel;
    probability: number;
  };
};

export {
  saveImageMutation,
  evaluateMutation,
  ResultImageService,
  ResultImageRoutes,
};
