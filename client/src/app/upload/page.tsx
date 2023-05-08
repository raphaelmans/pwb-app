"use client";
import AppCamera from "@features/camera/components/app-camera";
import UploadImageContainer from "@features/upload/upload-image-container";
import { Box, Center, Stack, Text } from "@mantine/core";

export default function UploadPage() {
  return (
    <Box bg="blue.2" h="100vh">
      <Center>
        <Stack>
          <Text size="xxl" component="h1">
            Upload
          </Text>
          <UploadImageContainer />
        </Stack>
      </Center>
    </Box>
  );
}
