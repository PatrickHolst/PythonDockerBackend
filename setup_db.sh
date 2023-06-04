if ! docker info >/dev/null 2>&1; then
    echo "Docker is not running, please start Docker before running this script."
    exit 1
fi

if ! aws dynamodb list-tables --endpoint-url http://localhost:8000 >/dev/null 2>&1; then
    docker run -p 8000:8000 amazon/dynamodb-local &
    echo "Starting DynamoDB..."
    sleep 2
fi

if [ "$1" == "--reset" ]; then
    if aws dynamodb describe-table \
        --table-name parents \
        --endpoint-url http://localhost:8000 \
        >/dev/null 2>&1; then
        aws dynamodb delete-table --table-name Parents --endpoint-url http://localhost:8000
        echo "Database deleted, Creating new Database"
    fi
fi

aws dynamodb create-table \
        --table-name parents \
        --attribute-definitions AttributeName=ParentId,AttributeType=S \
        --key-schema AttributeName=ParentId,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=20,WriteCapacityUnits=20 \
        --endpoint-url http://localhost:8000 &
    wait
    echo "Created Parents table"

aws dynamodb scan --table-name parents --endpoint-url http://localhost:8000

####################### CALCULATION TABLE ############################################

aws dynamodb create-table \
        --table-name calculations \
        --attribute-definitions AttributeName=calcId,AttributeType=S \
        --key-schema AttributeName=calcId,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=20,WriteCapacityUnits=20 \
        --endpoint-url http://localhost:8000 &
    wait
    echo "Created Calculations table"