/**************************
 * Sieve of Erastosthenes * (fast, memory efficient version)
 **************************
 * Does some magic, after which gP(n) is non-zero iff n is
 * prime. N is the value of the largest prime you will need.
 * Requires N / 16 bytes of memory.
 * WARNING! Only works for odd numbers; deal with even numbers
 * yourself!
 * If that is unacceptable, add "n==2||(n&1)&&" after the
 * first bracket in the gP() macro.
 * #include <string.h>
 * #include <math.h>
 */

void sieve_atkins(ll n)
{

    vector<bool> is_prime(n + 1);
    is_prime[2] = true;
    is_prime[3] = true;
    for (ll i = 5; i <= n; i++)
    {
        is_prime[i] = false;
    }
    ll lim = ceil(sqrt(n));
    for (ll x = 1; x <= lim; x++)
    {
        for (ll y = 1; y <= lim; y++)
        {
            ll num = (4 * x * x + y * y);
            if (num <= n && (num % 12 == 1 || num % 12 == 5))
            {
                is_prime[num] = true;
            }
            num = (3 * x * x + y * y);
            if (num <= n && (num % 12 == 7))
            {
                is_prime[num] = true;
            }

            if (x > y)
            {
                num = (3 * x * x - y * y);
                if (num <= n && (num % 12 == 11))
                {
                    is_prime[num] = true;
                }
            }
        }
    }
    for (ll i = 5; i <= lim; i++)
    {
        if (is_prime[i])
        {
            for (ll j = i * i; j <= n; j += i)
            {
                is_prime[j] = false;
            }
        }
    }
    int c = 0;
    for (ll i = 2; i <= n; i++)
    {
         if (is_prime[i])
         {
             cout<<i<<" ";
             c++;
         }
    }
    cout<<"Total : "<<c<<endl;
}

int main()
{
    freopen("out.in", "w", stdout);
    ll n;
    n = 100000000;
    cout<<"Following are the prime numbers below "<<n<<endl;
    sieve_atkins(n);
    cout<<endl;
    return 0;
}
