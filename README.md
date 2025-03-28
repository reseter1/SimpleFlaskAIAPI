# NULL AI Server API

## Giới thiệu
NULL AI Server API là một dịch vụ REST API được xây dựng bằng Flask để cung cấp các khả năng trí tuệ nhân tạo như trò chuyện (chat) và tạo hình ảnh thông qua các mô hình AI mạnh mẽ như Gemini và Bing Image Creator mà không cần sử dụng API key chính thức.

## Tính năng
- **Simple Response API**: Trả lời ngắn gọn và súc tích kèm emoji phù hợp
- **Detail Response API**: Trả lời chi tiết và đầy đủ thông tin
- **Image Generation API**: Tạo hình ảnh dựa trên mô tả văn bản
- **Dự phòng model**: Tự động chuyển đổi giữa các nhà cung cấp AI khi một dịch vụ không khả dụng

## Cài đặt

### Yêu cầu
- Python 3.12
- Pip

### Các bước cài đặt
1. Clone repository:
```bash
git clone https://github.com/reseter1/NULLAIServerAPI.git
cd NULLAIServerAPI
```

2. Tạo và kích hoạt môi trường ảo:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Cài đặt các thư viện phụ thuộc:
```bash
pip install -r requirements.txt
```

4. Tạo file .env từ file .env.example và cấu hình các biến môi trường:
```bash
cp .env.example .env
```

5. Chỉnh sửa file .env và thêm cookies cần thiết:
```
DEBUG=True
BingCookie=your_bing_cookie_here
Secure1PSID=your_secure_1psid_here
Secure1PSIDTS=your_secure_1psidts_here
LANG=vi
```

## Sử dụng

### Chạy ứng dụng
```bash
python run.py
```

### API Endpoints

#### 1. Simple Response
- **Endpoint**: `/api/v1/simple_response`
- **Method**: POST
- **Request Body**:
```json
{
  "message": "Câu hỏi của bạn ở đây"
}
```
- **Response**:
```json
{
  "text": "Câu trả lời ngắn gọn với emoji",
  "model": "Gemini Model"
}
```

#### 2. Detail Response
- **Endpoint**: `/api/v1/detail_response`
- **Method**: POST
- **Request Body**:
```json
{
  "message": "Câu hỏi của bạn ở đây"
}
```
- **Response**:
```json
{
  "text": "Câu trả lời chi tiết và đầy đủ",
  "model": "Gemini Model"
}
```

#### 3. Image Generation
- **Endpoint**: `/api/v1/image_response`
- **Method**: POST
- **Request Body**:
```json
{
  "message": "Mô tả hình ảnh bạn muốn tạo"
}
```
- **Response**:
```json
{
  "text": "URL của hình ảnh được tạo"
}
```

## Cấu hình
Dự án sử dụng các biến môi trường sau:
- `DEBUG`: Chế độ debug (True/False)
- `BingCookie`: Cookie _U của Bing, cần thiết cho việc tạo hình ảnh
- `Secure1PSID`: Cookie __Secure-1PSID của Google, cần thiết cho Gemini
- `Secure1PSIDTS`: Cookie __Secure-1PSIDTS của Google, cần thiết cho Gemini
- `LANG`: Ngôn ngữ mặc định của phản hồi (mặc định: vi)

## Triển khai
Dự án này có thể được triển khai trên Vercel hoặc các nền tảng tương tự. File `vercel.json` đã được cấu hình sẵn cho việc triển khai.

## Công nghệ sử dụng
- Flask: Framework web cho Python
- g4f: Thư viện cung cấp truy cập đến các mô hình AI miễn phí
- Flask-CORS: Hỗ trợ Cross-Origin Resource Sharing
- python-dotenv: Quản lý biến môi trường

## Lưu ý
- Dự án này sử dụng cookies để truy cập các dịch vụ AI. Cookies có thể hết hạn và cần được cập nhật định kỳ.
- Dự án này chỉ nên được sử dụng cho mục đích học tập và nghiên cứu.