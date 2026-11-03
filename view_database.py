from qdrant_client import QdrantClient

# Connect to your local Qdrant database
client = QdrantClient(path="./qdrant_gemini_768")

try:
    # Display available collections
    collections = client.get_collections()

    print("\n========== QDRANT DATABASE ==========")

    for collection in collections.collections:
        print(f"\nCollection: {collection.name}")

        info = client.get_collection(collection.name)
        print("Total stored points:", info.points_count)

        # Retrieve stored records
        points, next_offset = client.scroll(
            collection_name=collection.name,
            limit=100,
            with_payload=True,
            with_vectors=False
        )

        print("\nStored memories:")

        for point in points:
            print("\n---------------------------")
            print("ID:", point.id)
            print("Data:", point.payload)

finally:
    client.close()