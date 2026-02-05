import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

export const make_llm_call= async()=> {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

