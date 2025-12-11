from transformers import pipeline

def main():
    summarizer = pipeline(
        "summarization",
        model="digit82/kobart-summarization",
        tokenizer="digit82/kobart-summarization"
    )

    text = input("요약할 문장을 입력하세요:\n")
    result = summarizer(text, max_length=80, min_length=25, do_sample=False)

    print("\n=== 요약 결과 ===")
    print(result[0]["summary_text"])

if __name__ == "__main__":
    main()
