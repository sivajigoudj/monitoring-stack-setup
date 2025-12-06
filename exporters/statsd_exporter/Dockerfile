# Use a lightweight base image
FROM debian:bookworm-slim

# Install required dependencies
RUN apt-get update && apt-get install -y \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Copy the exporter tarball into the container and extract it directly to /bin
COPY statsd_exporter-0.27.2.linux-amd64.tar.gz /tmp
RUN tar -xzf /tmp/statsd_exporter-0.27.2.linux-amd64.tar.gz -C /bin --strip-components=1 \
    && rm /tmp/statsd_exporter-0.27.2.linux-amd64.tar.gz

# Change ownership and switch to a non-root user
RUN chown nobody:nogroup /bin/statsd_exporter
USER nobody

# Expose the default port (9102)
EXPOSE 9102

# Set the entrypoint to the exporter binary
ENTRYPOINT ["/bin/statsd_exporter"]

