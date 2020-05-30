FROM starefossen/github-pages

RUN apk add --no-cache gcc g++ make

COPY Gemfile .
COPY Gemfile.lock .

RUN bundle install

