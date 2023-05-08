import { Box, Center, Image, Loader, Text, Stack, Button } from "@mantine/core";
import { useEvaluate } from "@shared/hooks";
import { EvaluationResult } from "@shared/services";
import React, { useCallback, useMemo } from "react";
import { useDropzone } from "react-dropzone";

type Props = {};

const UploadImageContainer = (props: Props) => {
  const { evaluateImg, isMutating } = useEvaluate();
  const [image, setImage] = React.useState<string | null>(null);
  const [result, setResult] = React.useState<EvaluationResult | undefined>();
  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length === 1) {
      const file = acceptedFiles[0];

      const reader = new FileReader();
      reader.readAsDataURL(file);

      reader.onload = () => {
        const dataURI = reader.result;
        evaluateImg({
          datauri: dataURI as string,
        })
          .then((data) => setResult(data?.data))
          .finally(() => {
            setImage(dataURI as string);
          });
      };
    }
  }, []);

  const accept = useMemo(() => {
    return {
      "image/jpeg": [".jpg", ".jpeg"],
      "image/png": [".png"],
      "image/bmp": [".bmp"],
    };
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept,
    multiple: false,
  });

  if (isMutating) {
    <Center h={500} w={500} bg="blue.6">
      <Loader size={100} />
    </Center>;
  }

  if (image && result?.result) {
    return (
      <Stack>
        <Image
          src={image}
          maw={500}
          caption={
            result?.result.label == "GOOD" ? (
              <Stack spacing={0.5}>
                <Text fw="700" color="blue.8">
                  {result?.result?.label}
                </Text>
                <Text fw="500" color="blue.8">
                  {result?.result?.probability}
                </Text>
              </Stack>
            ) : (
              <Stack spacing={0.5}>
                <Text fw="700" color="red.8">
                  {result?.result?.label}
                </Text>
                <Text fw="500" color="red.8">
                  {result?.result?.probability}
                </Text>
              </Stack>
            )
          }
        />
        <Button {...getRootProps()}>Upload Another</Button>
      </Stack>
    );
  }
  return (
    <Center sx={{
        cursor: 'pointer'
    }} h={500} w={500} bg="blue.6" {...getRootProps()}>
      <input {...getInputProps()} />
      {isDragActive && !image && <p>Drop the files here ...</p>}
      {!isDragActive && !image && (
        <p>Drag 'n' drop some files here, or click to select files</p>
      )}
    </Center>
  );
};

export default UploadImageContainer;
