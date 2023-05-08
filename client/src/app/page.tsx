"use client";
import AppCamera from "@features/camera/components/app-camera";
import { Box, Center, Container, Stack, Text } from "@mantine/core";

export default function Home() {
  return (
    <Box bg="blue.2" h="100vh">
      <Center>
        <Stack>
          <Text size="xxl" component="h1">
            Home
          </Text>
          <AppCamera />
        </Stack>
      </Center>
    </Box>
  );
}
