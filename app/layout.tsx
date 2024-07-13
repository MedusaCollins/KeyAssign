import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: 'KeyAssign',
  description: 'KeyAssign, an open-source tool, simplifies computer control by adding a programmable layer between your keyboard and computer, allowing customization of actions for each key press, distinguishing it from standard macros.',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en'>
      <body className=' flex flex-col gap-5 px-5 items-center justify-center '>
        <Header />
        <span className=' w-full h-full '>
          {children}
        </span>
        <Footer />
      </body>
    </html>
  );
}
