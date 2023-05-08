"use client";
import { Button, Image, Stack } from "@mantine/core";
import React from "react";
import Webcam from "react-webcam";
import { v4 as uuidv4 } from "uuid";
import { BASE_DIMENSIONS, videoConstraints } from "../constants";
import useSWRMutation from "swr/mutation";
import {
  ResultImageRoutes,
  evaluateMutation,
  saveImageMutation,
} from "@shared/services";
import { useEvaluate } from "@shared/hooks";

type Props = {};

const AppCamera = (props: Props) => {
  const [base64Img, setBase64Img] = React.useState<string | null>(null);
  const [devices, setDevices] = React.useState<MediaDeviceInfo[]>([]);
  const webcamRef = React.useRef<Webcam>(null);

  const { evaluateImg, isMutating } = useEvaluate();

  const handleDevices = React.useCallback(
    (mediaDevices: MediaDeviceInfo[]) =>
      setDevices(mediaDevices.filter(({ kind }) => kind === "videoinput")),
    [setDevices]
  );

  const onCapture = React.useCallback(async () => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot({
        width: BASE_DIMENSIONS.width,
        height: BASE_DIMENSIONS.height,
      });

      if (imageSrc) {
        await evaluateImg({
          datauri: imageSrc,
        });
        // setBase64Img(imageSrc);
      }
    }
  }, [webcamRef]);
  React.useEffect(() => {
    navigator.mediaDevices.enumerateDevices().then(handleDevices);
  }, [handleDevices]);
  return (
    <Stack w="100%">
      {devices.map((device, key) => (
        <Webcam
          audio={false}
          height={400}
          ref={webcamRef}
          screenshotFormat="image/png"
          videoConstraints={{
            ...videoConstraints,
            deviceId: device.deviceId,
          }}
          key={key}
        />
      ))}
      {base64Img && <Image src={base64Img} />}
      <Button onClick={onCapture} loading={isMutating}>
        Capture photo
      </Button>
    </Stack>
  );
};

export default AppCamera;
