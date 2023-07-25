# Generated by Django 4.2.3 on 2023-07-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHoAAAB6CAMAAABHh7fWAAAAaVBMVEX///8AAAD5+flfX18RERHU1NT8/PyZmZlubm6wsLC/v7/v7+/z8/OdnZ3q6ur29vaAgIDk5OTd3d10dHSpqallZWVJSUm2trYmJiY3NzeTk5MwMDBTU1M9PT0YGBgrKyvIyMgeHh6JiYk0GPPXAAAJLklEQVRogb1b2YKqMAxVkU1kF0QFp/j/H3kl6ZJCWYe5eVIpPW1ysnTxcFgvEfPd3Gra8/F4bhsrd32WbuhmpZxYaL2PBnnXIYv/DjdixcsEK+RVXKK/wD3Zyc8ULspPbp/2BvZrHeNcVU1Z12VTVT0DlP6u4LeKdm65Fzt1xDMnsi+hRZ+3t92A76Tb4jZC5tT3SLP7LsB2IzvML85US+eSy6aN/WvgUyI6e4QL6BuED9E++aXJ5ZSb+7X3yLmC9PVwvTe7TDzkvVQ+RThFLEy8L7u/UtZeErKIztDxBSnDzcCxIM6HxKn4nijjK9MmVCvxh//sbQxwV262JlO/9d2bSk0cOis5QYItyOlAa1kyCsslV+YVtspMfU+LjW+2sjNbCxvH86O0isIqH2ftZ0u1b/GX1WTjyLVQWEoCxst6XtLgevpSzzldg5Q9aVrxRMwJ6k3YHDnnxHZC2XPzsQ32C+yPIp8r3so3YKeYEj78qyDNd0psNFCcmFRMKQyMTH+vKCSuqL8n/+qLLpOZPiLhVEef//JEC/XD0biUGrIIzMkCR7kKJ8j5Dy6qYSkyvp7gl5gru1xoMVu0vxo6m5MLegmfBg+K4WTOoiIoWXEloU9elrwaIZGRThEWRS1bCtyJjcP9wUx3QuovqdoKICVyNMBYWq6s9iJUOo+iGbhLMf8aliRYZXA7F4uVLcQpcMjxoMsJCVrCT08j6ypBtyjIl3bOQYCQbxwtOqW3BVlgY1CK3wtYnhE6ItPrbciHQz3oajqJeQotRhdZbWchDvI8VuOY1F9GRpcvGOmkZIQp2WxnueIG5q5fFfM36AKjYDFD2CsZW0mdMWxy5GeQlzy023XN6Ltx6JVlonsQ4DVgsoxo3ySugoMRvwM1/Bp66CITVEwQ89Leq18504gZvJXmYBjuKHQlFYQloVB3R75zF9GcrhqC6A6cFanx4JDi6Uk6hAk8IJGAAasxZAYRCD5Cim5EWSChTyPQdLlFq2+M39gMLMhGoBPZ7lQqn1wAjXw6Nrx6JukVmpUnOZuRsBJ3+n5HUjsP+WQGOoKitGGnGKM1LQwecq5RZ/jKTDTAwzRd6I41Aw1l0QsoCTZDKKIQZK7V0wgR6AG8A3OIejINjZUc7xPiPg1bR6lKUMnnYBAHgp1qRMwyDc3UxL6jhnGQMjCREwJ/rE2BGSyGT7ye1qahn7LzTvLeu0yqAeZ2NlUdtprqUdf3DHStzfPS8y/SWTJm7JscvE01OA/daANN+z5USMC7Tl69fwyNN8LeeejTS3PEqM8zXwKm/UdCIIo4RsXMQytXHkArQzrHo3E1EDfy966viq5VJqGd11DhNDtCJf+Ss2uGQSVt5WiPmgYPnLU6NKjxotSlT5KmEAxocgrtcN2WyVcga1v0mStYq6AhNJFyRtpHdzXZ9CqfDUsVGC3kU7DWZ/AMMvEZue9AJ3wBqUUppxQakvKR/HXN3sUkEe2+Z/L+jl4YdtDN7YnVJldrCtmDVxWYqrSQBWsw1n26yU+aXKSi9FSspt2XsyCMJTnME7S+X6ZocVcEmYDuLVNuBmhpNFvq4ITq0Hce7ougxxv4feAXoQsWKQ8Xlyv9gNWb1NpZf8mXPAhwGdKZXbUNrP56ZdmswcKKcLpcM9uG7JbZaW8zJyPITX/jRJHLN0MzyQ/l4QNRFWlPUqkSb7Bl40piKK5rovw66D6Z67fTGPTBucH+QznsGFNCJAcx9OvsfJyJ8pPQfEqmVVUpSd8N4jxsArsm2CsQeDX0yJQwG2EM7wLAz7BMgdK7dUQL8w7fFmgoguEdpz2KolwXiAYQoJ5mNmyEZpK1scn1OlEFwl0ybg9oV4YJUv3pcpfeBamr2Qu6kQQPjbHqwN0ZywsghmnDZwM0uCquML0xH4B17Y9K6abScQM0RDDI5tfOhx7GTWJPvmuPaXwDdKP3at7KucnxYaVncK/10FAlvsBnP2O65K3Q7dwRLq6HTqS34JrdvJmP6z1bjsJAtNXQQDKkFujbuNo7aHP1pPJ/B/1R9lXzNwj6QSCHONTOWmjUHvwYVGMeC2IpIsC0B3vYa6FJL0DikVcPvFJB96f7tJuh6a5sZeqPCGyxYR0Mpnn1FLQOGncYkDwQWd7jyKiVFj7ipmUvAqyDxkIVw1c77tS8a7KziBtReutV0Fi739Xn9+QVAjwoInvY+jycCa70CyR0Erq3Pn2I70Blifkrbo+93lCHI1zpHOlHfUWetjgLWIw+Znb1kZSMjPtNsZ0wGWVplpCLBXjCxHXGjO4ykIIwG1c71YabFvyUDZ0FmT5/0JVRZuMiqmVrkRnaiq8jkOkLTpJvlBL8VHjlOQRfG35oh4u6qIm5+UHsumM2furMky4jTJ8T9ASxKcHnvdzg3Mxizng6O3Hqob+MrXkQFSvrfNGZaiQO2vm2BCbs5dcV0DoPjmXz23Vvd/bYPgj5vbeK8ZE81nIFLSzOjqOCz6R6Ts48csXlo0K8WVKrLxP0h0Y4hNxKOeds5MpDzHK5tyAmmTbUUxcKPz16CxtF6jSpzf3B3AM/b2UDSzzm93GstceitcaWr4/Q+1aV9bld7CxNM/tyexb05mHDxBucnxuOgrmBczlmpl9CMoo6bBRXcRZcFBgKjyYP5RhZYrw5K+SdqExj882VVQxTIsj1VMy6XryHGfflXUgzvoO2/SSYcSM+tDNSO7SalqK2jRVqd6IufHjCu7dIKi7V1Xo4clKb3cPnV8I7I9dZQWz50u/uT8vbXvWi+zRfTckrgNsvNXKREz+28xdJg1Baotzjyvhd3ZCu/YkOU3Ln8Wefm7uHOCQxIx+JTY6Ko1/97HdLPQjV5UHz7unhqWYcbrrBOQ4u7+Oac688J2j8fYGx9w/Gstagcgfpdf78/oL0iGCVbkiCmGQX+t82oesoIqb12e6C+aznYrh5sClHrRC88afvxuD+j2G3eWdhQw9z/97QKJ++h6FfGe8/7C3g4D8yXsVggrkV7D4S6aRC4v25oVF86kr4xZ9+Yz8hE0UVjO+H7S0Bnmk50q/+IGyPCQZU9z/6lRLuYf/Rr6Q46GGg+Oa/+JUS8deMYUD/e5Fn6f/Nr5Tw+4R/na9Mwrdc/vBviuPC/rtfKblX1W8M/Q8xJG5Miy1giQAAAABJRU5ErkJggg==",
                max_length=500,
            ),
        ),
    ]
