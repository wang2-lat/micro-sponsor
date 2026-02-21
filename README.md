# micro-sponsor

A CLI tool to connect SaaS companies with micro-influencers for product promotion.

## Installation


## Usage

### For Companies

Create a new campaign:

View applications for your campaign:

### For Influencers

Browse available campaigns:

View campaign details:

Apply for a campaign:

## Features

- **Campaign Management**: Companies can post promotion opportunities with budget and target audience
- **Discovery**: Influencers can browse and filter available campaigns
- **Application System**: Influencers can apply with their rates and follower counts
- **Review Process**: Companies can review applicant profiles and metrics

## Data Storage

All data is stored locally in `.micro-sponsor/` directory as JSON files.
# 安装依赖
pip install -r requirements.txt

# 公司创建活动
python main.py create-campaign --company "MyAI" --product "ChatBot" --budget 1000 --audience "Developers"

# 网红浏览机会
python main.py list-campaigns

# 网红申请
python main.py apply --campaign-id abc123 --name "Jane" --platform "YouTube" --followers 10000 --rate 300

# 公司查看申请
python main.py list-applications --campaign-id abc123