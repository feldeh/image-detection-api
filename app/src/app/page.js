import Container from "@/components/Container";
import Heading from "@/components/Heading";
export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center max-w-2xl min-h-screen gap-5 p-10 m-auto md:max-w-4xl">
      <Heading />
      <Container />
    </main>
  );
}
